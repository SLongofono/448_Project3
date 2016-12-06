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

def testAllAssembleProfile():
        print "\nTesting getUserSongVectors() method... "
        test1 = testGetUserSongVectors()
        print "Passed." if test1 else "Failed."
                
        print "\nTesting getVectorFromTrack() method... "
        test2 = testGetVectorFromTrack()
        print "Passed." if test2 else "Failed."
        
        return (test1 and test2)

if __name__ == '__main__':
        testAllAssembleProfile()
