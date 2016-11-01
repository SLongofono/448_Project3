##@file Toy_Playlist.py
# @brief An example of using the Spotipy module to create and access a playlist
# @author Paul Lamere
# @details From the Spotipy documentation
#         Accessed October 2016
#         https://github.com/plamere/spotipy/blob/master/examples/user_playlists.py
#         Modified by Stephen Longofono
#         10/23/2016

import sys
import os
import subprocess
import spotipy
import spotipy.util as util


if len(sys.argv) > 2:
    username = sys.argv[1]
    playlist_name = sys.argv[2]
else:
    print("Usage: %s username playlist-name" % (sys.argv[0],))
    sys.exit()

token = util.prompt_for_user_token(username)

if token:
    sp = spotipy.Spotify(auth=token)
    sp.trace = False
    playlists = sp.user_playlist_create(username, playlist_name)

    # Get new songs to add from file
    try:
        songIDs = []
        songList = open('recommended.txt', 'r')
        for song in songlist:
            songIDs.append(song)
        songList.close()

    except:
        print "Error processing recommendations..."
        sys.exit()

    # Add songs
    try:
        for song in songIDs:
            sp.user_playlist_add_tracks(username, playlist_id, track_ids)
    except:
        print "Error adding songs to playlist..."
        sys.exit()

    # Add to list of already suggested songs
    x = open('oldsongs', 'a+')
    for song in songIDs:
            x.write(str(song))
            x.write('\n')
    x.close()

    # Remove recommended songs

else:
    print("Can't get token for", username)
