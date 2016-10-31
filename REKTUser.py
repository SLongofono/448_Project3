import Mutators
import traceback
import Variance
import functools
import os

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

    # I'm cheap but volatile
    def addData(self, newDataVector):
        for i in range(len(self.addVector)):
            self.addVector[i](newVal=newDataVector[i], debug=self.debug)

    def getSongDifferences(self, newSongVectors):
	return  map(functools.partial(Variance.getVariance, self.profile),  newSongVectors)


    def prettyPrintProfile(self):
        for i in range(10):
            print self.labels[i], ':'
            print self.profile[i]


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

        for i in self.profile:
            print i
        x.close()


    # I'm expensive but permenant
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

        except Exception as err:
            print 'Failed to save new profile...'
            traceback.print_exc()


if __name__ == '__main__':

	print "Test run..."

	# Basic setup
	print "Creating user..."
	tester = User(debug=True)

	print "User profile vector: "
	tester.prettyPrintProfile()

	print "Adding a new song vector: "
	testSong = [['Katy MF Perry', 'Bob Marley, Bob Vila, and Bob Ross'], ['Death Pop', 'Icelandic glam-folk'], 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0]
	print testSong
	tester.addData(testSong)
	print "Modified profile: "
	tester.prettyPrintProfile()

	print "Saving modified profile..."
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

	print "Generated test songs to compare against:"
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

	print "Most similar test song is: "
	print bestSong, " with a total difference ", bestVal

	print "Entering interactive demo..."

	command = "python Compare_Songs"
	os.system(command)
