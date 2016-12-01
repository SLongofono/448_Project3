import sys
import spotipy
import spotipy.util as util
import config_obj

user = config_obj.get_user()

##  getPlaylist
# @brief finds a playlist of a given name, or creates a new playlist if none are found
# @param user the spotify username of the user
# @param name the name of the playlist
# @return A spotify playlist id
# @details searches for a spotify playlist in the users account. Note, it can
#         see public playlists. If it finds a playlist matching the name paramater
#         it will return this playlists id. Otherwise, it will create a new playlist
#         with the name it passed, and return this newly created playlist's id.
#
def getPlaylist(user, name):
        scope = 'playlist-modify-public'
        usageToken = util.prompt_for_user_token(username=user['username'],
						client_id=user['client_id'],
						client_secret=user['client_secret'],
						redirect_uri=user['redirect_uri'],
						scope=scope)
        if usageToken:
		sp = spotipy.Spotify(auth=usageToken)
		user_playlists = sp.user_playlists(user['username'])
		for playlist in user_playlists['items']:
                        if playlist['name'] == name:
                                return playlist['id']
                #if no playlist has been found...
                return sp.user_playlist_create(user['username'], name, True)['id']

##  addToPlaylist
# @brief adds a list of songs to a spotify playlist
# @param user the spotify username of the user
# @param name the name of the playlist
# @param songs a list of spotify track ids
# @return none
# @details gets a playlist matching the name parameter. If none already exist, a new
#         playlist will be created.  Then adds the list of songs to the playlist.
#
def addToPlaylist(user, name, songs): #add songs parameter
        scope = 'playlist-modify-public'
        usageToken = util.prompt_for_user_token(username=user['username'],
						client_id=user['client_id'],
						client_secret=user['client_secret'],
						redirect_uri=user['redirect_uri'],
						scope=scope)
        if usageToken:
		sp = spotipy.Spotify(auth=usageToken)
		playlist_id = getPlaylist(user, name)
		sp.user_playlist_add_tracks(user['username'], playlist_id, songs)

#removes all tracks but does not delete playlist (leaves an empty playlist)

##  clearPlaylist
# @brief removes all songs from a user playlist
# @param user the spotify username of the user
# @param playlist_id the id of the spotify playlist
# @param songs a list of spotify track ids
# @details removes every song from a spotify playlist, leaving it empty. Note, the
#         playlist must be public for it to be found. The resulting playlist is not,
#         removed, just empty.
#
def clearPlaylist(user, playlist_id):
        scope = 'playlist-modify-public'
        usageToken = util.prompt_for_user_token(username=user['username'],
						client_id=user['client_id'],
						client_secret=user['client_secret'],
						redirect_uri=user['redirect_uri'],
						scope=scope)
        if usageToken:
                sp = spotipy.Spotify(auth=usageToken)
                playlist = sp.user_playlist(user['username'], playlist_id)
                track_ids = []
                for track in playlist['tracks']['items']:
                        track_ids.append(track['track']['id'])
                sp.user_playlist_remove_all_occurrences_of_tracks(user, playlist_id, track_ids)


#testing method
if __name__ == '__main__':
	if len(sys.argv) > 1:
		playlist_name = 'test_playlist'
		songs = ['6b2oQwSGFkzsMtQruIWm2p', '3SVAN3BRByDmHOhKyIDxfC', '045sp2JToyTaaKyXkGejPy', '7yMPuOVQEqpl7h1AQq4f2i', '5jafMI8FLibnjkYTZ33m0c']

		addToPlaylist(user, playlist_name, songs)
		#clearPlaylist(user, getPlaylist(user, playlist_name))

	else:
		print 'Usage: %s username' % (sys.argv[0],)
		sys.exit()
