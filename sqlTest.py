import sqlite3
import os
import traceback

localDB = "user.db"
db_exists = os.path.exists(localDB)

def initializeDB(conn, inFile):
	# FOR LATER
	# connect to spotify
	# pull songs per demo method
	# fill them in to appropriate tables

	# FOR NOW
	input = open(inFile, 'r')
	input.readline()
	labels = ['popularity', 'acousticness', 'danceability', 'energy', 'instrumentalness', 'key', 'liveness', 'valence']

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
	conn.execute("""
		CREATE TABLE artists (ID INTEGER PRIMARY KEY, name TEXT NOT NULL UNIQUE);
	""")

	# Create table for genres
	conn.execute("""
		CREATE TABLE genres (ID INTEGER PRIMARY KEY, name TEXT NOT NULL UNIQUE);
	""")

	for line in input:
		temp = line.split('###')[:-1]
		artists = temp[0][2:-2].split(',,')
		genres = temp[1][2:-2].split(',,')
		nums = temp[2:]
		artistQueries = [insertSingle('artists', 'name', x) for x in artists]
		print artistQueries
		genreQueries = [insertSingle('genres', 'name', x) for x in genres]
		print genreQueries
		valueQuery = insertMultiple('numerics', labels, nums)
		for i in artistQueries:
			try:
				conn.execute(i)

			# Catch duplicates and ignore
			except sqlite3.IntegrityError:
				pass

		for j in genreQueries:
			try:
				conn.execute(j)

			# Catch duplicates and ignore
			except sqlite3.IntegrityError:
				pass

		try:
			conn.execute(valueQuery)
		except:
			traceback.print_exc()

	input.close()

# Prep an insert SQL query for matched key-value pairs
def insertMultiple(table, keys, vals):
	keystr = '(' + ','.join(keys) + ')'
	valstr = '(' + ','.join(vals) + ')'
	return "INSERT INTO " + table + " " + keystr + " VALUES " + valstr + ";"

# Prep an insert query for a single key-value pair
def insertSingle(table, key, val):
	return "INSERT INTO " + table + " (" + key + ") VALUES ('" + val + "');"

with sqlite3.connect(localDB) as conn:
	if not db_exists:
		print "No valid user database found, creating new database..."
		initializeDB(conn, 'SongVectors.txt')

	print "Song vectors :"
	cursor = conn.execute("""
		SELECT * FROM numerics
	""")
	for i in cursor:
		print i

	print "Song Genres: "
	cursor = conn.execute("""
		SELECT * FROM artists
	""")
	for i in cursor:
		print i


	print "Song Artists: "
	cursor = conn.execute("""
		SELECT * FROM genres
	""")
	for i in cursor:
		print i

