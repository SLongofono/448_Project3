## @file Recommender.py
# @brief Script responsible for gathering, vetting, and adding songs to the user playlist
# @details This script is designed to be run periodically to generate new recommendations
#	for the user.  The script will instantiate a user, determine if the profile needs
#	to be updated, gather and filter songs, and finally load the songs that meet our
#	criterion into a special Spotify playlist.

## fetchSongs
# @brief Gather and process a new list of songs to be compared with the user profile
def fetchSongs():
	return

## filterSongs
# @brief Apply the 2 sigma filter to a list of songs to rule out outliers
def filterSongs(songsDict):
	return

## rankSongs
# @brief Rank filtered list of songs by difference from mean in ascending order
def rankSongs(songsDict):
	return

## updateRequired
# @brief Determine if a user's library and songs need to be updated
def updateRequired():
	return

## updateUser
# @brief Re-evaluates the user's library, profile, and standard deviations
#
def updateUser():
	return
