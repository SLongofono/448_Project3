## @file testDB.py
# @brief test script for database schema and integrity
# @details Run this as a standalone script to troubleshoot your setup,
#	or let the testing suite call it as a part of its checks.
#
import sqlite3
import config_obj
import time

labels = ['popularity', 'acousticness', 'danceability', 'energy', 'instrumentalness', 'key', 'liveness', 'valence']
user = config_obj.get_user()
localDB = config_obj.get_db()

print user
print localDB
conn = sqlite3.connect(localDB).cursor()

# Test columns, labels, data types, size
def testSchema(tableName, conn=conn, labels=labels):
	for label in labels:
		try:
			query =	"SELECT " + label + " FROM " + tableName
			conn.execute(query)
			temp = conn.fetchone()
			if temp == None:
				print "\nError: query returned nothing (check that it has been populated): ", query
				print
				return False

			print "Retrieved ", temp[0], " of type ", type(temp[0])
		except Exception as err:
			print "\nError in ", tableName, " using query ", query
			print type(err)
			print err
			print
			return False
	return True

# Test that an entry made its way into and out of the database
def testInsert(tableName, insertQuery, removeQuery, conn=conn):
	try:

		temp = list(conn.execute("SELECT * FROM " + tableName))
		beforeLength = len(temp)

		conn.execute(insertQuery)

		temp = list(conn.execute("SELECT * FROM " + tableName))
		afterLength = len(temp)

		if beforeLength == afterLength:
			print "\nError: insert failed to update length, using query:", insertQuery
			print
			return False
		else:
			print "Inserting, size changed from %d to %d" % (beforeLength, afterLength)

		conn.execute(removeQuery)
		temp = list(conn.execute("SELECT * FROM " + tableName))
		afterLength = len(temp)

		if beforeLength != afterLength:
			print "\nError: delete failed to update length, expected %d, got %d, using query: %s" % (beforeLength, afterLength, removeQuery)
			print
			return False
		else:
			print "Deleting, size %d now matches previous size %d" % (afterLength, beforeLength)

	except Exception as err:
		print "\nError in " + tableName + " with queries ", insertQuery, removeQuery
		print type(err)
		print err
		print
		return False
	return True

def go():
	numTests = 0
	numPassed = 0
	artist = "dummyartist" + str(int(time.time()))
	genre = "dummygenre" + str(int(time.time()))
	insertQueries = ["INSERT INTO numerics(popularity, acousticness, danceability, energy, instrumentalness, key, liveness, valence) VALUES(0,0,0,0,0,0,0,0)",
			 "INSERT INTO profile(popularity, acousticness, danceability, energy, instrumentalness, key, liveness, valence) VALUES(0,0,0,0,0,0,0,0)",
			 "INSERT INTO deviations(popularity, acousticness, danceability, energy, instrumentalness, key, liveness, valence) VALUES(0,0,0,0,0,0,0,0)",
			 "INSERT INTO weights(artists, genres, popularity, acousticness, danceability, energy, instrumentalness, key, liveness, valence) VALUES(1,1,0,0,0,0,0,0,0,0)",
			 "INSERT INTO artists(name) VALUES(" + "'" + artist + "')",
			 "INSERT INTO genres(name) VALUES(" + "'" + genre + "')"
			]
	removeQueries = ["DELETE FROM numerics WHERE popularity=0 AND key=0 AND acousticness=0 AND energy=0",
			 "DELETE FROM profile WHERE popularity=0 AND key=0 AND acousticness=0 AND energy=0",
			 "DELETE FROM deviations WHERE popularity=0 AND key=0 AND acousticness=0 AND energy=0",
			 "DELETE FROM weights WHERE popularity=0 AND key=0 AND acousticness=0 AND energy=0",
			 "DELETE FROM artists WHERE name=" + "'" + artist + "'",
			 "DELETE FROM genres WHERE name=" + "'" + genre + "'"]
	tables = ["numerics", "profile", "deviations", "weights", "artists", "genres"]

	print "\n\nTesting tables and types..."
	for tablename in tables[:-2]:
		numTests += 1
		if testSchema(tablename):
			numPassed += 1

	numTests += 2
	if testSchema(tableName='artists', labels=['name']):
		numPassed += 1

	if testSchema(tableName='genres', labels=['name']):
		numPassed += 1


	print "\n\nTesting insert..."

	for i in range(len(tables)):
		numTests += 1
		if testInsert(tableName=tables[i], insertQuery=insertQueries[i], removeQuery=removeQueries[i]):
			numPassed += 1

	return numTests, numPassed

if __name__ == "__main__":
	x,y = go()
	print "Tests: %d\nTests passed: %d\nPercentage: %f\n\n" % (x,y, (float(y)/x))
