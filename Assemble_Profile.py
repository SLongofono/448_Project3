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

## @var labels
# @brief A human-friendly list of the features in a user/song profile vector
labels = ['artists', 'genres', 'popularity', 'acousticness', 'danceability', 'energy', 'instrumentalness', 'key', 'liveness', 'valence']
scope = 'user-library-read'


##  dumpSongVectors
# @brief Write a list of song vectors to file for processing
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


##  getSongFeatures
# @brief Get the track data object for each song from a list of song ids
# @param sp The handle to the Spotipy wrapper associated with the current user
# @param ids A list of Spotify song ids
# @return A Spotify features object associated with the track
# @details Fetches the full length track object for each of the songs associated with the list of ids passed in.
#
def getSongFeatures(sp, ids):
	return sp.audio_features(ids)

##  getTracksUserAccount
# @brief Get the user's songs from their library
# @param sp The handle to the Spotipy wrapper associated with the current user
# @param limit Optional integer representing the number of tracks to fetch
# @param index Optional integer representing the index into the user's library to begin with
# @return A list of Spotify track objects associated with songs in the user's library
# @details Fetches up to limit songs from the user's saved songs library, beginning at the index indicated.
#
def getTracksUserAccount(sp, limit=20, index=0):
    return sp.current_user_saved_tracks(limit, index)

	
##  getUserSongVectors
# @brief Assembles a list of song vectors for a user
# @param user The spotify username of the user to fetch songs from
# @return A list of song vectors in the format produced by getVectorFromTrack()
# @details Steps through the first 100 songs of the user passed in, preparing a song vector
#         for each and aggregating the results into a list.  If the user does not have enough
#         songs, or if some other errors are preventing the API calls from completing, the
#         method will abandon its task after 3 failures
#
def getUserSongVectors(user):
	usageToken = util.prompt_for_user_token(user, scope)
	if usageToken:
		errorCount = 0
		arties = None
		trackid = None
		sp = spotipy.Spotify(auth=usageToken)
		vectors = []
		# Fetch up to the first 1000 songs to establish a data set
		for i in range (50):
			try:
				print "Getting batch..."
				library = getTracksUserAccount(sp, index=(20*i))
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


##  getVectorFromTrack
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
				songArtists.append(str(artist['name']))
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


if __name__ == '__main__':
    if len(sys.argv) > 1:
		user = sys.argv[1]

		print "\n\nGetting songs..."
		songs = getUserSongVectors(user)

		print "\n\nDumping songs..."
		dumpSongVectors(songs)
    else:
    	print "Usage: %s username" % (sys.argv[0],)
    	sys.exit()