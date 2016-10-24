import Mutators
import traceback

class User():
    def __init__(self, logfile="userProfile.txt", debug=False):
        self.logfile = logfile
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
        self.debug = debug

    # I'm cheap but volatile
    def addData(self, newDataVector):
        for i in range(len(self.addVector)):
            self.addVector[i](newVal=newDataVector[i], debug=self.debug)

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

    def prettyPrintProfile(self):
        for i in range(10):
            print self.labels[i], ':'
            print self.profile[i]

if __name__ == '__main__':
    tester = User(debug=True)
    tester.prettyPrintProfile()
    tester.addData([['Katy MF Perry', 'Bob Marley, Bob Vila, and Bob Ross'], ['Death Pop', 'Icelandic glam-folk'], 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0])
    tester.prettyPrintProfile()
    tester.saveStatus()
    tester.prettyPrintProfile()
