##@file REKTUser.py
# @author Stephen Longofono
# @brief
# @detail This file defines the User class which is used to generate and manipulate a user profile from
#         their Spotify profile

import Mutators
import traceback
import Variance
import functools
import Compare_Songs


##@class User
# @brief Manages creation and manipulation of a Spotify user profile
# @param in debug An optional Boolean parameter specifying whether or not to run in verbose mode
# @param in logfile An optional filename for a test file containing a user profile vector
# @detail The User class manages the local representation of a Spotify user, as aggregated from a
#         dataset composed of the songs in their Spotify library.  A profile vector represents the
#         average values for each of the features we track and recommend with, and is represented
#         locally in a text file (soon to be database)
class User():
	def __init__(self, logfile="userProfile.txt", debug=False):
		self.logfile = logfile
		self.debug = debug
		self.profile = None
		self.labels = ['artists', 'genres', 'popularity', 'acousticness', 'danceability', 'energy', 'instrumentalness', 'key', 'liveness', 'valence']
		self.processProfile(self.logfile)
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

	##@fn addData
	# @brief Processes a new song vector into the user profile vector
	# @param in newDataVector
	# @return void
	# @detail This method applies the mutator functions associated with each song feature to the features
	#         in newDataVector, incorporating their values in the volatile state within each mutator.  Note
	#         that changes are not applied to the user profile permenantly until saveStatus() is called.
	def addData(self, newDataVector):
		for i in range (len(self.addVector)):
			self.addVector[i](newVal=newDataVector[i], debug=self.debug)

	##@fn getSongDifferences
	# @brief Returns a list of the featurewise differences of each of a list of new song vectors and the user profile vector
	# @param in newSongVectors A list of song vectors to compare against
	# @return A list of lists representing the feature difference of each of the song vectors passed in.
	# @detail This method binds the Variance.getVariance() function to the user profile, and then Curries
	#         with each of the song vectors in newSongvectors.  See Variance.py for more details on how
	#         list features are handled versus value features.
	def getSongDifferences(self, newSongVectors):
		return  map(functools.partial(Variance.getVariance, self.profile),  newSongVectors)

	##@fn prettyPrintProfile
	# @brief Prints a user profile in a human-friendly way
	# @return void
	# @brief Prints a user profile in a human-friendly way (Label: value)
	def prettyPrintProfile(self):
		for i in range(10):
			print self.labels[i], ':'
			print self.profile[i]


	##@fn processProfile
	# @brief Reads in a user profile from a local logfile
	# @param in filename The text document which contains the user profile vector information.
	# @return void
	# @detail This method opens the file passed in and parses each line into the User.profile member.
	#         it is assumed that the filename passed in refers to a valid and accesible file in the
	#         CWD and that the file is properly formatted.  We used  {{a,,b,,c}} to denote lists, and
	#         each line is parsed as an element of the profile vector.
	def processProfile(self, filename):
		print 'Processing user profile data...'
		self.profile = []
		x = open(filename, 'r')
		artists = x.readline()[2:-3].split(',,')
		genres = x.readline()[2:-3].split(',,')
		self.profile.append(artists)
		self.profile.append(genres)
		for line in x:
			self.profile.append(float(line))
		x.close()


	##@fn saveStatus
	# @brief Saves the current user profile vector to disk
	# @return void
	# @detail This method aggregates the new values in the mutator functions and writes them to
	#         the user profile logfile, preserving the state for future access by our program.
	#         Each element in the profile vector is written to its own line.  Values are written
	#         directly, and lists are written as {{a,,b,,c}} to represent the list [a,b,c].
	def saveStatus(self):
		# Add unique entries to existing artist and genre lists
		self.profile[0] += Mutators.getUniques(self.profile[0], self.addVector[0]())
		self.profile[1] += Mutators.getUniques(self.profile[1], self.addVector[1]())

		# Average in numerical values
		for i in range(2, len(self.profile)):
			self.profile[i] = (self.profile[i] + self.addVector[i]())/2
		try:
			x = open(self.logfile, 'w')
			x.write('{{' + ',,'.join(self.profile[0]) + '}}')
			x.write('\n')
			x.write('{{' + ',,'.join(self.profile[1]) + '}}')
			x.write('\n')
			for i in range(2, len(self.profile)):
				x.write(str(self.profile[i]))
				x.write('\n')
			x.close()

		except:
			print 'Failed to save new profile...'
			traceback.print_exc()


# Demonstration and ad-hoc testing below
if __name__ == '__main__':
	import os
	import sys
	user = sys.argv[1]

	print "\n\nTest run..."

	# Basic setup
	print "\n\nCreating user..."
	tester = User(debug=True)

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


	print "\n\nEntering interactive demo..."

	command = "python Compare_Songs.py " + user
	os.system(command)
