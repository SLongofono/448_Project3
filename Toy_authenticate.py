## @file Toy_authenticate.py
# @brief An example of using the Spotipy module to authenticate
# @author Paul Lamere
# @details From the Spotipy documentation
#             Accessed October 2016
#             https://spotipy.readthedocs.io

import sys
import spotipy
import spotipy.util as util
import config_obj

user = config_obj.get_user()
for key, val in user.iteritems():
	print type(val)

scope = 'user-library-read'

usageToken = util.prompt_for_user_token(username=user['username'],
					client_id=user['client_id'],
					client_secret=user['client_secret'],
					redirect_uri=user['redirect_uri'],
					scope=scope)

if usageToken:
	sp = spotipy.Spotify(auth=usageToken)
	results = sp.current_user_saved_tracks()
	for item in results['items']:
		track = item['track']
		print track['name'] + ' - ' + track['artists'][0]['name']
else:
	print "Could not retrieve token for ", user
