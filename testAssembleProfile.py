import sys
import spotipy
import spotipy.util as util
import config_obj
import Assemble_Profile

user = config_obj.get_user()

def testGetUserSongVectors():
        print "Getting song vectors from user library"
        songVectors = Assemble_Profile.getUserSongVectors(user, numCalls=1, numEntries=1)
        return (len(songVectors) > 0)

def testGetVectorFromTrack():
        scope = 'user-library-read'
        usageToken = util.prompt_for_user_token(username=user['username'],
						client_id=user['client_id'],
						client_secret=user['client_secret'],
						redirect_uri=user['redirect_uri'],
						scope=scope)
        if usageToken:
		sp = spotipy.Spotify(auth=usageToken)
                #Assemble_Profile.getVectorFromTrack(sp, 
                song_id = '6b2oQwSGFkzsMtQruIWm2p'
                
                search = sp.search('radiohead', limit=1,)
                track = search['tracks']['items'][0]
                
                print "Building vector from track"
                featureVector = Assemble_Profile.getVectorFromTrack(sp, sp.audio_features([track['id']])[0], track['artists'])
                
                expectedVector = [['Radiohead'], ['alternative rock', 'indie rock', 'melancholia', 'permanent wave', 'rock'], 400, 0.0102, 0.515, 0.43, 0.000141, 7, 0.129, 0.096]
                
                print "Comparing to expected values"
                return (featureVector == expectedVector)

def go():
        print "\nTesting getUserSongVectors() method... "
        test1 = testGetUserSongVectors()
        print "Passed." if test1 else "Failed."
                
        print "\nTesting getVectorFromTrack() method... "
        test2 = testGetVectorFromTrack()
        print "Passed." if test2 else "Failed."
        numTests = 2
	numPassed = 0
	if test1:
		numPassed += 1
	if test2:
		numPassed += 1

	print "Number of tests: %d\t\tTests Passed: %d\t\tPercentage: %f\n" % (numTests,numPassed,((100.0*numPassed)/numTests))
        return (numTests, numPassed)

if __name__ == '__main__':
        x,y = go()
	print "Number of tests: %d\t\tTests Passed: %d\n" % (x,y)
