## @file populatePlaylist.py
# @brief Gathers, vets and creates a playlist for songs
# @details This script strings together the process of gathering songs to process,
#	computing the weighted differnce from average, and adding the least different
#	songs to a playlist on the user's Spotify account.  This script is called after
#	updating the user's database in the run.py script
#
import spotipy
import REKTUser
import PlaylistGenerator
import Recommender
import Variance
import config_obj
from collections import OrderedDict

## @var newSongCount
# @brief Minimum amount of new songs to add to playlist
newSongCount = 100

## @var threshold
# @brief Maximum weighted difference allowed for songs that make it into the list
threshold = 250


## filterDifference
# @brief Simple helper function to filter out dictionary entries
#	with differences beyond a threshold value
# @param songsDict A dictionary of the form Spotify track ID: weighted feature differences
# @param threshold An optional parameter specifying the upper bound for the cum of the weighted
#	feature differences
# @return A list of track IDs associated with songs that had total difference less than the
#	threshold
# @details This is a helper method used to filter a dictionary type.  The input dictionary
#	contains the weighted feature-wise difference of each track ID, the sum of which
#	must be below the threshold for the song to be considered a match.
#
def filterDifference(songsDict, threshold=threshold):
	results = []
	for id, difference in songsDict.iteritems():
		if sum(difference) < threshold:
			results.append(id)
	return results

user = config_obj.get_user()

tester = REKTUser.User()
weights = Variance.getNewWeight(tester.stdDevs)
results = OrderedDict()
while(len(results) < newSongCount):
	songs = Recommender.fetch(user, tester.profile)
	results.update(Recommender.rankSongs(songs, tester.profile, tester.stdDevs, weights))

newTrackIDs = filterDifference(results)
print "Adding tracks: ", newTrackIDs

PlaylistGenerator.addToPlaylist(user, '448 DEMO', newTrackIDs[:100])
