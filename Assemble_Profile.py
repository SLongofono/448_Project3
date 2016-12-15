## @file Assemble_Profile.py
# Assemble Profile script
# @brief Prepares a database of song features from track objects on the user's Spotify account.  First step
#        in setting up our recommendation system.
# @details This script accesses the user's account and assembles up to the first 1000 songs in their library.
#         From each song, the features we care about are extracted and packed into an easily parsed format
#         in "SongVectors.txt".
#
# @instructions Run this script after setting up a Spotify developer account, exporting your credentials to
#               the system path, and setting up Spotipy in a virtual Python environment.
import sys
import spotipy
import spotipy.util as util
import time
import pprint
import traceback
import config_obj
import os
import sqlite3

user = config_obj.get_user()
localDB = config_obj.get_db()
db_exists = os.path.exists(localDB)


## @var labels
# @brief A human-friendly list of the features in a user/song profile vector
labels = ['artists', 'genres', 'popularity', 'acousticness', 'danceability', 'energy', 'instrumentalness', 'key', 'liveness', 'valence']
scope = 'user-library-read'


## dumpSongVectors
# @brief Write a list of song vectors to file for processing/debugging
# @param vectors A list of song vectors in the format produced by getVectorFromTrack()
# @return void
# @details Steps through the list of song vectors and writes each to SongVectors.txt on its own
#         line.  This file represents the "database" of known liked songs for a user, against
#         which we can prepare a user profile and make decisions about new songs.
#         Entries are separated by '###'.  Since artists and genres are lists, they are
#         recorded within '{{' '}}' and delimited by ',,'.  For example, the list [1,2,3] would
#         be encoded as {{1,,2,,3}}
#
def dumpSongVectors(vectors):
    x = open('SongVectors.txt', 'w')
    for i in labels:
    	x.write(i)
    	x.write('###')
    x.write('\n')
    for vector in vectors:
        # Write artists and genres lists in a special format we can easily parse later
        x.write('{{' + ',,'.join(vector[0]) + '}}')
        x.write('###')
        x.write('{{' + ',,'.join(vector[1]) + '}}')
        x.write('###')
        for i in range(2, len(vector)):
            x.write(str(vector[i]))
            x.write('###')
        x.write('\n')
    x.close()


## getSongFeatures
# @brief Get the track data object for each song from a list of song ids
# @param sp The handle to the Spotipy wrapper associated with the current user
# @param ids A list of Spotify song ids
# @return A Spotify features object associated with the track
# @details Fetches the full length track object for each of the songs associated with the list of ids passed in.
#
def getSongFeatures(sp, ids):
	return sp.audio_features(ids)


## getTracksUserAccount
# @brief Get the user's songs from their library
# @param sp The handle to the Spotipy wrapper associated with the current user
# @param limit Optional integer representing the number of tracks to fetch
# @param index Optional integer representing the index into the user's library to begin with
# @return A list of Spotify track objects associated with songs in the user's library
# @details Fetches up to limit songs from the user's saved songs library, beginning at the index indicated.
#
def getTracksUserAccount(sp, limit=20, index=0):
    return sp.current_user_saved_tracks(limit, index)


## getUserSongVectors
# @brief Assembles a list of song vectors for a user
# @param user The spotify username of the user to fetch songs from
# @return A list of song vectors in the format produced by getVectorFromTrack()
# @details Steps through the first 100 songs of the user passed in, preparing a song vector
#         for each and aggregating the results into a list.  If the user does not have enough
#         songs, or if some other errors are preventing the API calls from completing, the
#         method will abandon its task after 3 failures
#
def getUserSongVectors(user, numCalls=50, numEntries=20):
	usageToken = util.prompt_for_user_token(username=user['username'],
						client_id=user['client_id'],
						client_secret=user['client_secret'],
						redirect_uri=user['redirect_uri'],
						scope=scope)
	if usageToken:
		errorCount = 0
		arties = None
		trackid = None
		sp = spotipy.Spotify(auth=usageToken)
		vectors = []
		# Fetch up to the first 1000 songs to establish a data set
		for i in range (numCalls):
			try:
				print "Getting batch..."
				library = getTracksUserAccount(sp, index=(numEntries*i))
				print "Processing songs..."
				if len(library['items']) > 0:
					for item in library['items']:
						trackid = item['track']['id']
						arties = item['track']['artists']
						temp = getVectorFromTrack(sp, sp.audio_features([trackid])[0], arties)
						vectors.append(temp)
				else:
					#Delay so we don't get locked out of API
					time.sleep(0.5)
			except:
				# get out if we continually fail
				print "Error!"
				traceback.print_exc()
				errorCount += 1
				if errorCount >= 3:
					break
		return vectors
	else:
		print "Could not retrieve token for ", user
		sys.exit()


## getVectorFromTrack
# @brief Assembles a vector of feature values for a track
# @param sp The handle to the Spotipy wrapper associated with the current user
# @param features A Spotify feature object associated with the track in question
# @param artists A list of Spotify artist objects that are associated with the track in question
# @return A list of qualities associated with the track in question
# @details A vector of features that our app cares about is assembled from the multitude of information in the Spotify objects.
#         The features passed in include a number of qualities curated by Spotify to classify a song with.  The artist(s) that
#         are associated with the song in question each provide contributions to a list of artist names, a list of genres, and
#         an integer representing overall popularity rating.  This popularity is averaged (to account for weird collaborations).
#
def getVectorFromTrack(sp, features, artists):
	songArtists = []
	genres = []
	popularity = 0
	for entry in artists:
		artist = sp.artist(entry['id'])
		for i in artist['genres']:
			genres.append(str(i))
			temp = str(artist['name'])
			if not temp in songArtists:
				songArtists.append(str(artist['name']).replace("'", ''))
			popularity += artist['popularity']
	popularity /= len(artists)
	trackVector = [
		songArtists,
		genres,
		popularity,
		features['acousticness'],
		features['danceability'],
		features['energy'],
		features['instrumentalness'],
		features['key'],
		features['liveness'],
		features['valence']
		]
	return trackVector


## insertMultiple
# @brief Prep an insert SQL query for multipe matched key-value pairs
# @param table A string representing the name of the table for the query
# @param keys A list of strings representing column names within the table
# @param vals A list of values corresponding to the columns passed in
# @return A list of strings representing SQL insert queries using the keys and values passed in
# @details This method prepares strings for SQL insert queries.  It is assumed that the keys and
#	values are aligned.
def insertMultiple(table, keys, vals):
	# Join not smart enough to cast so we need to do it manually
	keystr = '(' + ','.join(map(str, keys)) + ')'
	valstr = '(' + ','.join(map(str, vals)) + ')'
	return "INSERT INTO " + table + " " + keystr + " VALUES " + valstr + ";"

## insertSingle
# @brief Prep an insert query for a single key-value pair
# @param table A string representing the name of the table for the query
# @param keys A list of strings representing column names within the table
# @param vals A list of values corresponding to the columns passed in
# @return A string representing a SQL insert query using the keys and values passed in
# @details This method prepares a string for a SQL insert query.  It is assumed that the keys and
#	values are aligned.
def insertSingle(table, key, val):
	return "INSERT INTO " + table + " (" + str(key) + ") VALUES ('" + val + "');"


## initializeDB
# @brief Set up and populate a database of song vectors from the user's library
# @param conn A SQLite3 connection object attached to an open database file
# @param songVectors A list of song vectors to be added to the new database
# @return void
# @details This method is responsible for creating a local database with tables to store song feature
#	vectors, artists, genres, standard deviations, and user profile values.  It is assumed that
#	the tables do not already exist.
def initializeDB(conn, songVectors):

	"""Schema
		numerics   - rows represent individual songs, columns are numeric features associated with the songs
		artists    - rows represent unique artist strings
		genres	   - rows represent unique genre strings
		profile    - rows represent the average value of each column in numerics
		deviations - rows represent the standard deviation of each column in numerics
		weight     - single row, columns represent the weight of each of the 10 features, composed of
			     artists, genres, popularity, acousticness, danceability, energy, instrumentalness, key, liveness, and valence"""

	# Create table for numeric values
	conn.execute("""CREATE TABLE numerics (	ID INTEGER PRIMARY KEY,
						popularity DECIMAL NOT NULL,
						acousticness DECIMAL NOT NULL,
						danceability DECIMAL NOT NULL,
						energy DECIMAL NOT NULL,
						instrumentalness DECIMAL NOT NULL,
						key INT NOT NULL,
						liveness DECIMAL NOT NULL,
						valence DECIMAL NOT NULL
						);""")

	# Create table for artists
	conn.execute("""CREATE TABLE artists (ID INTEGER PRIMARY KEY, name TEXT NOT NULL);""")

	# Create table for genres
	conn.execute("""CREATE TABLE genres (ID INTEGER PRIMARY KEY, name TEXT NOT NULL UNIQUE);""")

	# Create table for user profile
	conn.execute("""CREATE TABLE profile(popularity DECIMAL NOT NULL,
					     acousticness DECIMAL NOT NULL,
					     danceability DECIMAL NOT NULL,
					     energy DECIMAL NOT NULL,
					     instrumentalness DECIMAL NOT NULL,
					     key INT NOT NULL,
					     liveness DECIMAL NOT NULL,
					     valence DECIMAL NOT NULL);""")

	# Create table for user profile std deviations
	conn.execute("""CREATE TABLE deviations(popularity DECIMAL NOT NULL,
						acousticness DECIMAL NOT NULL,
						danceability DECIMAL NOT NULL,
						energy DECIMAL NOT NULL,
						instrumentalness DECIMAL NOT NULL,
						key INT NOT NULL,
						liveness DECIMAL NOT NULL,
						valence DECIMAL NOT NULL);""")

	# Create table for user profile weights
	conn.execute("""CREATE TABLE weights(	artists DECIMAL NOT NULL,
						genres DECIMAL NOT NULL,
						popularity DECIMAL NOT NULL,
						acousticness DECIMAL NOT NULL,
						danceability DECIMAL NOT NULL,
						energy DECIMAL NOT NULL,
						instrumentalness DECIMAL NOT NULL,
						key INT NOT NULL,
						liveness DECIMAL NOT NULL,
						valence DECIMAL NOT NULL);""")


	for song in songVectors:
		nums = song[2:]
		artistQueries = [insertSingle('artists', 'name', x) for x in song[0]]
		genreQueries = [insertSingle('genres', 'name', x) for x in song[1]]
		valueQuery = insertMultiple('numerics', labels[2:], song[2:])
		for i in artistQueries:
			try:
				conn.execute(i)

			# Catch duplicates and move on
			except sqlite3.IntegrityError:
				pass

		for j in genreQueries:
			try:
				conn.execute(j)

			# Catch duplicates and move on
			except sqlite3.IntegrityError:
				pass

		try:
			conn.execute(valueQuery)
		except:
			traceback.print_exc()

	# Make it so
	conn.commit()






## updateSongsDB
# @brief Adds new songs in the user's library to the database, skipping over duplicates.
# @param conn, a handle into a SQLite3 local database
# @param songVectors A list comprised of song vectors, of the form [[artists:string], [genres:string], 10*float]
# @return void
# @details This method is responsible for updating a user's library in the local database.  This method
#	is inefficient, but the alternative is manually checking that each song locally is in the user's
#	tracks, resulting in an API call for each (much worse).  songVectors are assumed to be in the proper format
#
def updateSongsDB(conn, songVectors):
	for song in songVectors:
		nums = song[2:]
		artistQueries = [insertSingle('artists', 'name', x) for x in song[0]]
		genreQueries = [insertSingle('genres', 'name', x) for x in song[1]]
		valueQuery = insertMultiple('numerics', labels[2:], song[2:])
		for i in artistQueries:
			try:
				conn.execute(i)
			except sqlite3.IntegrityError:
				pass

		for j in genreQueries:
			try:
				conn.execute(j)

			except sqlite3.IntegrityError:
				pass

		try:
			conn.execute(valueQuery)
		except:
			traceback.print_exc()
		# Save all changes
		conn.commit()


if __name__ == '__main__':
	with sqlite3.connect(localDB) as conn:
		if (not db_exists):
			print "\nNo valid user database found, creating new database...\n"
			print "\nGathering song vectors...\n"
			songVectors = getUserSongVectors(user)
			initializeDB(conn, songVectors)

		else:
			print "\nGathering Song Vectors...\n"
			print "\nUpdating User Profile...\n"
			songVectors = getUserSongVectors(user)
			updateSongsDB(conn,songVectors)

		# Give some feedback for debugging
		print "Song numeric vectors :"
		cursor = conn.execute("SELECT * FROM numerics")
		for i in cursor:
			print i

		print "Song Artists: "
		cursor = conn.execute("SELECT * FROM artists")
		for i in cursor:
			print i


		print "Song Genres: "
		cursor = conn.execute("SELECT * FROM genres")
		for i in cursor:
			print i
