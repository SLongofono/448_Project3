import sys
import spotipy
import spotipy.util as util
import config_obj
import PlaylistGenerator

user = config_obj.get_user()

def testNewPlaylist():
        scope = 'playlist-modify-public'
        usageToken = util.prompt_for_user_token(username=user['username'],
						client_id=user['client_id'],
						client_secret=user['client_secret'],
						redirect_uri=user['redirect_uri'],
						scope=scope)
        if usageToken:
		sp = spotipy.Spotify(auth=usageToken)
		
		#run twice to make sure not creating multiple playlists
		for i in range(2):
                        print "Creating/searching for playlist 'test_playlist'"
                        
                        PlaylistGenerator.getPlaylist(user, 'test_playlist')
                        
                        user_playlists = sp.user_playlists(user['username'])
                        playlistNum = 0
                        for playlist in user_playlists['items']:
                                if playlist['name'] == 'test_playlist':
                                        playlistNum += 1
                        if playlistNum != 1:
                                return False;
                            
                        print "Playlist found"
                
                return True;
                

def testAddSongs():
        #some pre-pulled song ids to test with
        songs = ['6b2oQwSGFkzsMtQruIWm2p', '3SVAN3BRByDmHOhKyIDxfC', '045sp2JToyTaaKyXkGejPy', '7yMPuOVQEqpl7h1AQq4f2i', '5jafMI8FLibnjkYTZ33m0c']
        
        print "Finding playlist"
        playlist_id = PlaylistGenerator.getPlaylist(user, 'test_playlist')
        PlaylistGenerator.clearPlaylist(user, playlist_id)
        print "Adding songs to playlist"
        PlaylistGenerator.addToPlaylist(user, 'test_playlist', songs)
        
        scope = 'playlist-modify-public'
        usageToken = util.prompt_for_user_token(username=user['username'],
						client_id=user['client_id'],
						client_secret=user['client_secret'],
						redirect_uri=user['redirect_uri'],
						scope=scope)
        if usageToken:
		sp = spotipy.Spotify(auth=usageToken)
		
		#playlist_id = PlaylistGenerator.getPlaylist(user, 'test_playlist')
		playlist = sp.user_playlist(user['username'], playlist_id)
		
		print "Checking songs were added to playlist"
                for id in songs:
                        foundMatch = False
                        for track in playlist['tracks']['items']:
                                if id == track['track']['id']:
                                        foundMatch = True
                        if foundMatch == False:
                                return False
                
                playlistLength = 0
                for track in playlist['tracks']['items']:
                    playlistLength += 1
                
                return (playlistLength == 5)

def testClearPlaylist():
        songs = ['6b2oQwSGFkzsMtQruIWm2p', '3SVAN3BRByDmHOhKyIDxfC', '045sp2JToyTaaKyXkGejPy', '7yMPuOVQEqpl7h1AQq4f2i', '5jafMI8FLibnjkYTZ33m0c']
        PlaylistGenerator.addToPlaylist(user, 'test_playlist', songs)
        
        print "Finding playlist"
        playlist_id = PlaylistGenerator.getPlaylist(user, 'test_playlist')
        print "Clearing playlist"
        PlaylistGenerator.clearPlaylist(user, playlist_id)
        
        scope = 'playlist-modify-public'
        usageToken = util.prompt_for_user_token(username=user['username'],
						client_id=user['client_id'],
						client_secret=user['client_secret'],
						redirect_uri=user['redirect_uri'],
						scope=scope)
        if usageToken:
		sp = spotipy.Spotify(auth=usageToken)
		
		#playlist_id = PlaylistGenerator.getPlaylist(user, 'test_playlist')
		playlist = sp.user_playlist(user['username'], playlist_id)
		
		print "Checking that playlist is cleared"
		playlistLength = 0
		for track in playlist['tracks']['items']:
                        playlistLength += 1
                
                return (playlistLength == 0)
            
def testAllPlaylist():
        print "\nTesting ability to create new playlist... "
        test1 = testNewPlaylist()
        print "Passed." if test1 else "Failed."
        
        print "\nTesting ability to add songs to a playlist... "
        test2 = testAddSongs()
        print "Passed." if test2 else "Failed."
        
        print "\nTesting ability to remove all songs from a playlist... " 
        test3 = testClearPlaylist()
        print "Passed." if test3 else "Failed."
        
        return (test1 and test2 and test3)

if __name__ == '__main__':
        testAllPlaylist()
