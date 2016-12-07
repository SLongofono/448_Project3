import spotipy
import REKTUser
import PlaylistGenerator
import Recommender
import Variance
import config_obj
from collections import OrderedDict

# Minimum amount of new songs to add to playlist
newSongCount = 100

# Maximum weighted difference allowed for songs that make it into the list
threshold = 250

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
