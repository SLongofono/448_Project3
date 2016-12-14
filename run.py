## @file run.py
# @brief Single entry point for our recommender system
# @details This script runs Assemble_Profile.py to initiate or update the user profile database,
#	and then calls populatePlaylist.py to generate a new playlist of songs.  It allows a single
#	script to kick off the recommendation system.

import os

commands = ['python Assemble_Profile.py', 'python populatePlaylist.py']

for command in commands:
	os.system(command)

