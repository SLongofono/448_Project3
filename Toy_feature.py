import sys
import spotipy
import spotipy.util as util


def getArtist(sp, artist, numTracks, startTrack):
	return sp.search(artist, numTracks, startTrack, 'track')
	

def getSongFeatures(sp, ids):
	return sp.audio_features(ids)

scope = 'user-library-read'

if len(sys.argv) > 1:
	user = sys.argv[1]
else:
	print "Usage: %s username" % (sys.argv[0],)
	sys.exit()


usageToken = util.prompt_for_user_token(user, scope)

if usageToken:
	sp = spotipy.Spotify(auth=usageToken)
	results = getArtist(sp, 'Frank Zappa', 5, 0)['tracks']['items']
	print "Frank Zappa tracks:"
	for entry in results:
		print entry['artists'][0]['name'], ' : ', entry['name'], ' : ', entry['id']

	firstTrack = results[0]
	for a, b in firstTrack.iteritems():
		print a
		print b

	print firstTrack['id']

	features = getSongFeatures(sp, [firstTrack['id']])
	for a, b, in features[0].iteritems():
		print a, b

else:
	print "Could not retrieve token for ", user
	sys.exit()
