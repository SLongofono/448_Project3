## @file REKTUser.py
# REKTUser
# @author Stephen Longofono
# @brief The user class for the recommendation system
# @details This file defines the User class which is used to generate and manipulate a user profile from
#         their Spotify profile

import Mutators
import traceback
import Variance
import functools
import Compare_Songs
import sqlite3
import config_obj
user = config_obj.get_user()
localDB = config_obj.get_db()


## @class User
# @brief Manages creation and manipulation of a Spotify user profile
# @param debug An optional Boolean parameter specifying whether or not to run in verbose mode
# @param logfile An optional filename for a test file containing a user profile vector
# @details The User class manages the local representation of a Spotify user, as aggregated from a
#         dataset composed of the songs in their Spotify library.  A profile vector represents the
#         average values for each of the features we track and recommend with, and is represented
#         locally in a text file (soon to be database)
class User():
	def __init__(self, logfile="userProfile.txt", debug=False):
		self.db = sqlite3.connect(localDB)
		# Set up the interface to always return strings if possible, since in general utf(x) != str(x)
		self.db.text_factory = str
		self.logfile = logfile
		self.debug = debug
		self.profile = None
		self.stdDev = None
		self.labels = ['artists', 'genres', 'popularity', 'acousticness', 'danceability', 'energy', 'instrumentalness', 'key', 'liveness', 'valence']
		self.addVector =[
                            Mutators.artistMutator,
                            Mutators.genreMutator,
                            Mutators.popularityMutator,
                            Mutators.acousticnessMutator,
                            Mutators.danceabilityMutator,
                            Mutators.energyMutator,
                            Mutators.instrumentalnessMutator,
                            Mutators.keyMutator,
                            Mutators.livenessMutator,
                            Mutators.valenceMutator
			]
		self.processProfile()

	## addData
	# @brief Processes a new song vector into the user profile vector
	# @param newDataVector
	# @return void
	# @details This method applies the mutator functions associated with each song feature to the features
	#         in newDataVector, incorporating their values in the volatile state within each mutator.  Note
	#         that changes are not applied to the user profile permenantly until saveStatus() is called.
	def addData(self, newDataVector):
		for i in range (len(self.addVector)):
			self.addVector[i](newVal=newDataVector[i], debug=self.debug)


	## getSongDifferences
	# @brief Returns a list of the featurewise differences of each of a list of new song vectors and the user profile vector
	# @param newSongVectors A list of song vectors to compare against
	# @return A list of lists representing the feature difference of each of the song vectors passed in.
	# @details This method binds the Variance.getVariance() function to the user profile, and then Curries
	#         with each of the song vectors in newSongvectors.  See Variance.py for more details on how
	#         list features are handled versus value features.
	def getSongDifferences(self, newSongVectors):
		return  map(functools.partial(Variance.getVariance, self.profile),  newSongVectors)


	## prettyPrintProfile
	# @brief Prints a user profile in a human-friendly way
	# @return void
	# @brief Prints a user profile in a human-friendly way (Label: value)
	def prettyPrintProfile(self):
		if len(self.profile) > 2:
			for i in range(10):
				print self.labels[i], ':'
				print self.profile[i]
		else:
			print "Profile has not been set up in database yet, did you forget to run calculateAverages()?"


	## processProfile
	# @brief Reads in a user profile from a local database, updates profile database
	# @return void
	# @details This method opens the database associate with the user and parses out the user profile
	#	  into the User.profile member.  After recalculating the average, the user profile is saved
	#	  in the profile table.  It is assumed that the database passed in refers to a valid
	#	  and accesible file in the working directory and that it has been initialized with the
	#         schema detailed in Assemble_Profile.py.
	def processProfile(self):
		print 'Processing user profile data...'
		self.profile = []
		self.profile.append(map(lambda x: x[0], self.db.execute("SELECT name FROM artists")))
		self.profile.append(map(lambda x: x[0], self.db.execute("SELECT name FROM genres")))
		self.calculateAverages()
		self.calculateStandardDeviation()
		weight = getNewWeight(self.stdDev):
		print "Saving user profile..."
		self.db.execute("INSERT INTO profile(popularity,acousticness,danceability,energy,instrumentalness,key,liveness,valence) VALUES(?,?,?,?,?,?,?,?);", tuple(self.profile[2:]))
		self.db.execute("INSERT INTO deviatons(popularity,acousticness,danceability,energy,instrumentalness,key,liveness,valence) VALUES(?,?,?,?,?,?,?,?);", tuple(self.stdDev))
		self.db.execute("INSERT INTO weights(popularity,acousticness,danceability,energy,instrumentalness,key,liveness,valence) VALUES(?,?,?,?,?,?,?,?);", tuple(weight[2:]))
		self.db.commit()

	## calculateAverages
	# @brief update the user profile with the current average of numeric values in the user database
	# @return void
	# @details This method is used to evaluate the mean of each column in the "numerics" table for the
	#	user.  It is assumed that the database has been initialized, and that the "numerics" table
	# 	already exists.
	def calculateAverages(self):
		print 'Assembling averages...'
		payload = [self.db.execute("SELECT " + x + " FROM NUMERICS;") for x in self.labels[2:]]

		averages = []
		for column in payload:
			data = [x[0] for x in column]
			averages.append(sum(data)/len(data))
		print averages
		self.profile = self.profile[:2] + averages
		self.prettyPrintProfile()

	##	calculateStandardDeviation
	# @brief Calculates and updates the Current StdDev of the saved song vectors
	# @return void
	# #details This method is used to evaluate the stddev of each column of the NUMERICS table;
	# 	each column being representative of all of the user's audio features associated with the
	#	they've saved. Requires DB initialization and that the NUMERICS table has been filled.
	def caluculateStandardDeviation(self):
		print 'Assembling Standard Deviations ...'
		payload = [self.db.execute("SELECT " + x + " FROM NUMERICS;") for x in self.labels[2:]]
		stdDev = []
		for column in payload:
			mean=sum(column)/len(column)
		self.stdDev.append((sum( (x-mean)**2.0 for x in row ) / float(len(row)) )**0.5))

	## saveStatus
	# @brief Saves the current user profile vector and any new songs to the user database
	# @return void
	# @details This method aggregates the new values in the mutator functions and writes them to
	#         the user profile logfile, preserving the state for future access by our program.
	#         Songs are then added to the user database, and the standard deviations are updated
	def saveStatus(self):
		# Average new values into profile
		for i in range(2, len(self.profile)):
			newVals = self.addVector[i]()
			self.profile[i] = (self.profile[i] + sum(newVals))/(1 + len(newVals))

		# Identify unique artists and genres to add to database
		newArtists = Mutators.getUniques(self.profile[0], self.addVector[0]())
		newGenres = Mutators.getUniques(self.profile[1], self.addVector[1]())

		# Attempt to add in new artists and genres
		for each in newArtists:
			try:
				self.db.execute("INSERT INTO artists(name) values(?);", each)
			except:
				pass

		for each in newGenres:
			try:
				self.db.execute("INSERT INTO genres(name) values(?);", each)
			except:
				pass


		# Add in new numerical values to db
		newSongs = zipAll([x() for x in self.addVector[2:]])
		print "Saving new songs..."
		for song in newSongs:
			try:
				# Note that this is special sqlite3 syntax, and would not otherwise work in Python
				self.db.execute("INSERT INTO numerics(popularity, acousticness,danceability,energy,instrumentalness,key,liveness,valence) VALUES(?,?,?,?,?,?,?,?)", song)
			except:
				pass

		# TODO Add in new standard deviations to db

		print "Saving user profile..."
		for i in range(len(self.profile[2:])):
			self.db.execute("UPDATE profile SET " + self.labels[i+2] + "=" + str(self.profile[i+2]) + ";")

		self.db.commit()

## zipAll
# @brief Helper function which implements zip for an arbitrary number of lists
# @param columns a list of lists representing columns in a table
# @return a list of tuples, each tuple representing the ith row in the column set
# @details This implements zip on an arbitrary number of columns.  The built in zip
#	will accept any number of explicitly defined lists to zip over, but it does
#	not include a way to pass in a list of those lists.
def zipAll(columns):
	results = []
	i = 0
	while i < len(columns[0]):
		row = [x[i] for x in columns]
		results.append(tuple(row))
		i += 1
	return results

# Demonstration and ad-hoc testing below
if __name__ == '__main__':
	import os

	print "\n\nTest run..."

	# Basic setup
	print "\n\nCreating user..."
	tester = User(debug=True)

	tester.calculateAverages()

	print "\n\nUser profile vector: "
	tester.prettyPrintProfile()

	print "\n\nAdding a new song vector: "
	testSong = [['Katy MF Perry', 'Bob Marley, Bob Vila, and Bob Ross'], ['Death Pop', 'Icelandic glam-folk'], 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0]
	print testSong
	tester.addData(testSong)
	print "\n\nModified profile: "
	tester.prettyPrintProfile()

	print "\n\nSaving modified profile..."
	tester.saveStatus()

	# Comparison
	# Build test cases
	newSongs = []
	artists = ['The Unicorns','New Artist 1','new Artist 2','of Montreal','Mr. Bungle','RJD2', 'TV On The Radio', 'The Beatles', 'The Who', 'The Rolling Stones']
	genres = ['blues-rock','ok indie','power pop','psychedelic rock','slow core','space rock','alternative pop','jangle pop','new wave','post-hardcore','post-punk','punk','rock','shoegaze','uk post-punk','album rock','art rock','classic funk rock','classic rock','dance rock','folk rock','glam rock','hard rock','mellow gold','new wave pop','permanent wave','pop christmas','protopunk','singer-songwriter','soft rock','funk','soul','new weird america','pop rock','post-grunge','big beat','downtempo','folk-pop','ambeat','electro house','classic soundtrack','library music','spytrack','indie garage rock','indie poptimism','metropopolis','shimmer pop','compositional ambient','post rock','australian dance','electroclash','filter house','pop']
	for i in range(10):
		newSong = [
			[artists[i]],
			[genres[i]],
			i,
			i,
			i,
			i,
			i,
			i,
			i,
			i
			]
		newSongs.append(newSong)

	print "\n\nGenerated test songs to compare against:"
	for i in newSongs:
		print i

	diffs = tester.getSongDifferences(newSongs)
	bestSong = None
	bestVal = 200000
	for i in range(len(newSongs)):
		print "Artist: ", newSongs[i][0][0], " Difference: ", sum(diffs[i])
		if sum(diffs[i]) < bestVal:
			bestVal = sum(diffs[i])
			bestSong = newSongs[i][0][0]

	print "\n\nMost similar test song is: "
	print bestSong, " with a total difference ", bestVal

	print "\n\nFetching songs to compare against..."
#	newReleases = Compare_Songs.compareNewReleases(user, lim=5)
	newReleases = Compare_Songs.compareSearch(user, query="Elvis Costello", lim=10)


	print "\n\nNew songs: "
	print newReleases
	for i in newReleases:
		print i


	diffs = tester.getSongDifferences(newReleases)
	bestSong = None
	bestVal = 200000
	for i in range(len(newReleases)):
		if len(newReleases[i][0]) > 0:
			print "Artist: ", newReleases[i][0][0], " Difference: ", sum(diffs[i])
			if sum(diffs[i]) < bestVal:
				bestVal = sum(diffs[i])
				bestSong = newReleases[i][0][0]

	print "\n\nMost similar new song is: "
	print bestSong, " with a total difference ", bestVal
