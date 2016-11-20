import sys
import spotipy
import spotipy.util as util

#creates or finds playlist with that name
def getPlaylist(user, name):
        scope = 'playlist-modify-public'
        usageToken = util.prompt_for_user_token(user, scope)
        if usageToken:
		sp = spotipy.Spotify(auth=usageToken)
		user_playlists = sp.user_playlists(user)
		for playlist in user_playlists['items']:
                        if playlist['name'] == name:
                                return playlist['id']
                #if no playlist has been found...
                return sp.user_playlist_create(user, name, True)['id']
            
#playlist does not have to already exist - handled by getPlaylist function
#songs = list of track ids
def addToPlaylist(user, name, songs): #add songs parameter
        scope = 'playlist-modify-public'
        usageToken = util.prompt_for_user_token(user, scope)
        if usageToken:
		sp = spotipy.Spotify(auth=usageToken)
		playlist_id = getPlaylist(user, name)
		sp.user_playlist_add_tracks(user, playlist_id, songs)

#removes all tracks but does not delete playlist (leaves an empty playlist)
def clearPlaylist(user, playlist_id):
        scope = 'playlist-modify-public'
        usageToken = util.prompt_for_user_token(user, scope)
        if usageToken:
                sp = spotipy.Spotify(auth=usageToken)
                playlist = sp.user_playlist(user, playlist_id)
                track_ids = []
                for track in playlist['tracks']['items']:
                        track_ids.append(track['track']['id'])
                sp.user_playlist_remove_all_occurrences_of_tracks(user, playlist_id, track_ids)

#temporary test method
def temp_test(user, query):
        scope = 'playlist-modify-public'
        usageToken = util.prompt_for_user_token(user, scope)
        if usageToken:
                sp = spotipy.Spotify(auth=usageToken)
                results = sp.search(query, 5)
                
                for track in results['tracks']['items']:
                        print track['id']

if __name__ == '__main__':
	if len(sys.argv) > 1:
		user = sys.argv[1]
		playlist_name = 'test_playlist'
		songs = ['6b2oQwSGFkzsMtQruIWm2p', '3SVAN3BRByDmHOhKyIDxfC', '045sp2JToyTaaKyXkGejPy', '7yMPuOVQEqpl7h1AQq4f2i', '5jafMI8FLibnjkYTZ33m0c']
		
		addToPlaylist(user, playlist_name, songs) 
		#clearPlaylist(user, getPlaylist(user, playlist_name))
		
	else:
		print 'Usage: %s username' % (sys.argv[0],)
		sys.exit()

