## @file Compare_Songs.py
# Compare Songs
# @brief Functions associated with the collection of tracks to compare against
# @details This file describes the methods by which we collect songs to process
#               against our user profile.
import sys
import spotipy
import spotipy.util as util
import Assemble_Profile
import config_obj

# Get user credentials object
user = config_obj.get_user()

## @var scope
# @brief describes the permissions associated with the authorization token
scope = 'user-library-read'


##  compareFeatured
# @brief Gets songs from featured playlists and returns a list of audio features 
# @param user a user to establish a usageToken
# @param lim the number of playlists to retrieve
# @param debug prints debug info if true		
# @return A list of vectorized versions of audio features
# @details Grabs a number of spotify's featured playlists, as specified by the lim
#         parameter. For each track within each playlist, it gets the audio features,
#         converts it to a vector, and finally returns a list of all the vectors
#
def compareFeatured(user, lim=20, debug=True):
	usageToken = util.prompt_for_user_token(username=user['username'],
						client_id=user['client_id'],
						client_secret=user['client_secret'],
						redirect_uri=user['redirect_uri'],
						scope=scope)
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


##  compareNewReleases
# @brief Compares new releases with the user's agrregated preferences
# @param lim the number of new releases to compare
# @return A list of vectorized versions of audio features
# @details grabs a number of spotify's new releases, as specified by the lim
#         parameter. For each track, it gets the audio features, converts it
#         to a vector, and finally returns a list of all the vectors
#
def compareNewReleases(user, lim=20, debug=False):
	usageToken = util.prompt_for_user_token(username=user['username'],
						client_id=user['client_id'],
						client_secret=user['client_secret'],
						redirect_uri=user['redirect_uri'],
						scope=scope)
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


##  compareSearch
# @brief Gets songs from a search query and returns a list of audio features
# @param user a user to establish a usageToken
# @param query a string to be used with the spotify search feature
# @param lim the number of search results to retrieve
# @param debug prints debug info if true
# @return A list of vectorized versions of audio features
# @details searches spotify with the given query, and gets as many results as specified
#         by the lim parameter. For each track, it gets the audio features, converts it
#         to a vector, and finally returns a list of all the vectors
#
def compareSearch(user, query, lim=20, debug=False):
	usageToken = util.prompt_for_user_token(username=user['username'],
						client_id=user['client_id'],
						client_secret=user['client_secret'],
						redirect_uri=user['redirect_uri'],
						scope=scope)
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
		

# a menu system to test the various comparison methods
if __name__ == '__main__':
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

