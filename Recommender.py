## @file Recommender.py
# @brief Script responsible for gathering, vetting, and adding songs to the user playlist
# @details This script is designed to be run periodically to generate new recommendations
#	for the user.  The script will instantiate a user, determine if the profile needs
#	to be updated, gather and filter songs, and finally load the songs that meet our
#	criterion into a special Spotify playlist.

import spotipy
import spotipy.util as util
import Assemble_Profile
import config_obj
import Variance
import functools
import random
from collections import OrderedDict

user = config_obj.get_user()
scope = 'user-library-read'

# number of songs to fetch
songLimit = 25


## fetch
# @brief Convenience wrapper to collect songs from both new and featured songs
def fetch(user):
	results = {}
	results.update(fetchNewSongs(user))
	results.update(fetchFeaturedSongs(user))
	return results

## fetchNewSongs
# @brief Gather and process a list of new songs to be compared with the user profile
def fetchNewSongs(user, lim=songLimit):
	usageToken = util.prompt_for_user_token(username=user['username'],
						client_id=user['client_id'],
						client_secret=user['client_secret'],
						redirect_uri=user['redirect_uri'],
						scope=scope)
	vectors = {}
	if usageToken:
		sp = spotipy.Spotify(auth=usageToken)
		startPosition = random.randint(0, 100)
		results = sp.new_releases(limit=songLimit, offset=startPosition)

		for album in results['albums']['items']:
			tracks = sp.album_tracks(album['id'])
			for track in tracks['items']:
				try:
					featureVector = Assemble_Profile.getVectorFromTrack(sp, sp.audio_features([track['id']])[0], track['artists'])
					vectors[track['id']] = featureVector
				except: pass

	return vectors


## fetchFeaturedSongs
# @brief Gather and process a list of featured songs to be compared with the user profile
def fetchFeaturedSongs(user, lim=songLimit):
	usageToken = util.prompt_for_user_token(username=user['username'],
						client_id=user['client_id'],
						client_secret=user['client_secret'],
						redirect_uri=user['redirect_uri'],
						scope=scope)
	vectors = {}
	if usageToken:
		sp = spotipy.Spotify(auth=usageToken)
		# Grab the first 5 featured playlists
		startPosition = random.randint(0, 20)
		results = sp.featured_playlists(limit=5, offset=startPosition)

		for playlist in results['playlists']['items']:
			results = sp.user_playlist_tracks(user="spotify", playlist_id=playlist['id'])

			for item in results['items']:
				track = item['track']
				try:
					featureVector = Assemble_Profile.getVectorFromTrack(sp, sp.audio_features([track['id']])[0], track['artists'])
					vectors[track['id']] = featureVector
					if len(vectors) >= songLimit:
						return vectors
				except:
					pass

	return vectors


## filterSongs
# @brief Apply the 2 sigma filter to a list of songs to rule out outliers
# @details Assumes the songsDict is an ordered dictionary
def filterSongs(songsDict, averages, stddevs):
	#songVecs = [x[2:] for x in songsDict.values()]
	songVecs = songsDict.values()
	songIds = songsDict.keys()
	results = {}
	filterVec = Variance.filter2Sigma(songVecs, averages, stddevs)
	for i in range(len(filterVec)):
		results[songIds[i]] = songVecs[i]
	return results


## rankSongs
# @brief Rank filtered list of songs by difference from mean in ascending order
# @details Assumes the songsDict is an ordered dictionary
def rankSongs(songsDict, averages, stddevs, weights):
	# filter out garbage
	newDict = filterSongs(songsDict, averages, stddevs)

	# compute difference and apply weights
	songVecs = newDict.values()
	songIds = newDict.keys()
	differences = map(functools.partial(Variance.getWeightedDifference, base=averages, weighting=weights), songVecs)
	result = {}
	for i in range(len(differences)):
		result[songIds[i]] = differences[i]

	# sort results
	return OrderedDict(sorted(result.items(), key=lambda t: t[1]))

## updateRequired
# @brief Determine if a user's library and songs need to be updated
def updateRequired():
	return

## updateUser
# @brief Re-evaluates the user's library, profile, and standard deviations
#
def updateUser():
	return

if __name__ == "__main__":

#	for a,b in vec2.iteritems():
#		print a, b

	average = [[],[],0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0]
	stddevs = [1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0]
	weights = [1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0]
	vec2 = fetchNewSongs(user)

	x = rankSongs(vec2, average, stddevs, weights)
	for a,b in x.iteritems():
		print "Song id: ", a
		print "Weighted difference: " ,b
		print "Sum of difference: ", sum(b)
