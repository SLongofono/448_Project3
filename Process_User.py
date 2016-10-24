import sys
import spotipy
import spotipy.util as util
import time
import pprint

labels = ['artists', 'genres', 'popularity', 'acousticness', 'danceability', 'energy', 'instrumentalness', 'key', 'liveness', 'valence']


def getArtist(sp, artist, numTracks, startTrack):
	return sp.search(artist, numTracks, startTrack, 'track')


def getSongFeatures(sp, ids):
	return sp.audio_features(ids)

def getSongsUser(sp, user, limit=20, index=0):
    return sp.current_user_saved_tracks(limit, index)

def getPlaylistsUser():
    pass

def getVectorFromTrack(sp, features, artists):
    songArtists = []
    genres = []
    popularity = 0
    for entry in artists:
        artist = sp.artist(entry['id'])
        for i in artist['genres']:
            genres.append(str(i))
        songArtists.append(str(artist['name']))
        popularity += artist['popularity']
    popularity /= len(artists)
    trackVector = [
    songArtists,
    genres,
    popularity,
    features['acousticness'],
    features['danceability'],
    features['energy'],
    features['instrumentalness'],
    features['key'],
    features['liveness'],
    features['valence']
    ]
    return trackVector

def processSongs(sp, ids, artists, waitTime):
    if len(ids) != len(artists):
        raise IndexError
    songs = []
    for i in range(len(ids)):
        features = sp.audio_features([ids[i]])
        metadata = sp.search(artists[i])
        songs.append(getVectorFromTrack())
        time.sleep(waitTime)

def dumpSongVectors(vectors):
    x = open('SongVectors.txt', 'w')
    for i in labels:
        x.write(i)
        x.write('###')
    x.write('\n')
    for vector in vectors:
        for i in range(len(vector)):
            x.write(str(vector[i]))
            x.write(',')
        x.write('\n')
    x.close()

scope = 'user-library-read'

if len(sys.argv) > 1:
	user = sys.argv[1]
else:
	print "Usage: %s username" % (sys.argv[0],)
	sys.exit()


usageToken = util.prompt_for_user_token(user, scope)

if usageToken:
    arties = None
    trackid = None
    sp = spotipy.Spotify(auth=usageToken)
    vectors = []
    for i in range (10):
        try:
            library = getSongsUser(sp, user, index=(20*i))
            for item in library['items']:
                #print item['track']['name']
                trackid = item['track']['id']
                arties = item['track']['artists']
                temp = getVectorFromTrack(sp, sp.audio_features([trackid])[0], arties)
                vectors.append(temp)
                time.sleep(2)
        except:
                pass
            #for artist in item['track']['artists']:
            #    print artist['name']
    dumpSongVectors(vectors)

else:
	print "Could not retrieve token for ", user
	sys.exit()
