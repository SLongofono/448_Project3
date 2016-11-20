## @file Toy_feature.py
# @brief An example of using the Spotipy module to authenticate
# @author Paul Lamere
# @details From the Spotipy documentation
#             Accessed October 2016
#             https://github.com/plamere/spotipy/blob/master/examples/audio_features.py

import sys
import spotipy
import spotipy.util as util
import config_obj

user=config_obj.get_user()
db = config_obj.get_db()

def getArtist(sp, artist, numTracks, startTrack):
	return sp.search(artist, numTracks, startTrack, 'track')

def getArtistId(sp, artist):
	temp = sp.search(q=artist, type='artist')
	print temp['artists']['items'][0]['id']
	return temp['artists']['items'][0]['id']

def getSongFeatures(sp, ids):
	return sp.audio_features(ids)

scope = 'user-library-read'

usageToken = util.prompt_for_user_token(username=user['username'],
					client_id=user['client_id'],
					client_secret=user['client_secret'],
					redirect_uri=user['redirect_uri'],
					scope=scope)

if usageToken:
	sp = spotipy.Spotify(auth=usageToken)
	artistObj = getArtist(sp, 'Frank Zappa',5, 0)
	results = artistObj['tracks']['items']

	print "Artist info: "
	artie =  sp.artist(getArtistId(sp, 'Big Data'))
	print "Name: ", artie['name']
	print "Genres: ", artie['genres']
	print "Popularity: ", artie['popularity']
	print "Spotify Id: ", artie['id']

	print artie['name'], "tracks:"
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
