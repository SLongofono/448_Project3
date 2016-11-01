##@file Toy_authenticate.py
# @brief An example of using the Spotipy module to authenticate
# @author Paul Lamere
# @details From the Spotipy documentation
#             Accessed October 2016
#             https://spotipy.readthedocs.io

import sys
import spotipy
import spotipy.util as util

scope = 'user-library-read'

if len(sys.argv) > 1:
	user = sys.argv[1]
else:
	print "Usage: %s username" % (sys.argv[0],)
	sys.exit()


usageToken = util.prompt_for_user_token(user, scope)

if usageToken:
	sp = spotipy.Spotify(auth=usageToken)
	results = sp.current_user_saved_tracks()
	for item in results['items']:
		track = item['track']
		print track['name'] + ' - ' + track['artists'][0]['name']
else:
	print "Could not retrieve token for ", user
