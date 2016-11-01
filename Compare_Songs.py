import sys
import spotipy
import spotipy.util as util
import Assemble_Profile

scope = 'user-library-read'

##@fn
# @brief Gets songs from a search query and returns a list of audio features 
# @param in user a user to establish a usageToken
# @param in query a string to be used with the spotify search feature
# @param in lim the number of search results to retrieve
# @param in debug prints debug info if true
# @return out a list of vectorized versions of audio features
# @detail searches spotify with the given query, and gets as many results as specified
#         by the lim parameter. For each track, it gets the audio features, converts it
#         to a vector, and finally returns a list of all the vectors
#
def compareSearch(user, query, lim=20, debug=False):
	usageToken = util.prompt_for_user_token(user, scope)
	if usageToken:
		sp = spotipy.Spotify(auth=usageToken)
		results = sp.search(query, limit=lim)
		
		vectors = []
		for track in results['tracks']['items']:
			try:
				featureVector = Assemble_Profile.getVectorFromTrack(sp, sp.audio_features([track['id']])[0], track['artists'])
				vectors.append(featureVector)
			except: pass
		
		if debug:
			print vectors
		
		return vectors


##@fn
# @brief Gets songs from featured playlists and returns a list of audio features 
# @param in user a user to establish a usageToken
# @param in lim the number of playlists to retrieve
# @param in debug prints debug info if true		
# @return out a list of vectorized versions of audio features
# @detail grabs a number of spotify's featured playlists, as specified by the lim
#         parameter. For each track within each playlist, it gets the audio features,
#         converts it to a vector, and finally returns a list of all the vectors
#
def compareFeatured(user, lim=20, debug=True):
	usageToken = util.prompt_for_user_token(user, scope)
	if usageToken:
		sp = spotipy.Spotify(auth=usageToken)
		results = sp.featured_playlists(limit=lim)
		
		vectors = []
		for playlist in results['playlists']['items']:
			results = sp.user_playlist_tracks(user="spotify", playlist_id=playlist['id'])
			
			for item in results['items']:
				track = item['track']
				try:
					featureVector = Assemble_Profile.getVectorFromTrack(sp, sp.audio_features([track['id']])[0], track['artists'])
					vectors.append(featureVector)
				except: pass
			
				
		if debug:
			print vectors
			
		return vectors


##@fn
# @brief Compares new releases with the user's agrregated preferences
# @param in lim the number of new releases to compare
# @return out a list of vectorized versions of audio features
# @detail grabs a number of spotify's new releases, as specified by the lim
#         parameter. For each track, it gets the audio features, converts it
#         to a vector, and finally returns a list of all the vectors
#
def compareNewReleases(user, lim=20, debug=False):
	usageToken = util.prompt_for_user_token(user, scope)
	if usageToken:
		sp = spotipy.Spotify(auth=usageToken)
		results = sp.new_releases(limit=lim)
		
		vectors = []
		for album in results['albums']['items']:
			tracks = sp.album_tracks(album['id'])
			for track in tracks['items']:
				try:
					featureVector = Assemble_Profile.getVectorFromTrack(sp, sp.audio_features([track['id']])[0], track['artists'])
					vectors.append(featureVector)
				except: pass
		
		if debug:
			print vectors
			
		return vectors
		

# a menu system to test the various comparison methods
if __name__ == '__main__':
	if len(sys.argv) > 1:
		user = sys.argv[1]
		command = raw_input("Enter the number associated with the desired command:\n   1. Compare with New Releases\n   2. Compare with Featured Playlists\n   3. Compare with Search\n")
		if command == "1":
			lim = int(raw_input("How many new releases would you like to compare (Max 50)? "))
			if lim <= 50 and lim > 0:
				compareNewReleases(user, lim, True)
			else:
				print "Invalid input"
		
		elif command == "2":
			lim = int(raw_input("How many new playlists would you like to compare (Max 10)?\n(Note: Playlists can be very long, requesting more than 1 playlist may take a long time)\n"))
			if lim <= 10 and lim > 0:
				compareFeatured(user, lim, True)
			else:
				print "Invalid input"
			
		elif command == "3":
			query = raw_input("Please enter search query: ")
			lim = int(raw_input("How many new releases would you like to compare (Max 50)? "))
			if lim <= 50 and lim > 0:
				compareSearch(user, query, lim, True)
			else:
				print "Invalid input"
		
		else:
			print "Invalid command"
		
	else:
		print "Usage: %s username" % (sys.argv[0],)
		sys.exit()


