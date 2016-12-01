## @package setup.sh
# This is a short script written to verify that the dependencies of our project are present.
# Our project makes use of virtualenv, python, and Spotipy.  This script assumes that python
# and virtualenv are installed and in the system path.
#
# Instructions
#
# 1. clone our project source into a git directory and navigate into the root
# 2. Run 'chmod +x setup.sh' from the command line to allow this script to execute
# 3. Run this script './setup.sh'
# 4. If all is well, your environment is ready
# 5. Start your virtual environment by typing 'source spotifyVenv/bin/activate'
# 6. Stop your virtual environment by typing 'deactivate'
#
# Created by Stephen Longofono
#

#!/bin/bash
clear

echo " [ checking virtualenv version... ] "
# Virtualenv allows a virtual python environment to be created, in which you can run scripts
# and install packages in isolation from the rest of the system.  We need it because KU IT
# is rightfully restrictive about what packages we are allowed to install on the Linux machines (none).
# Specifically, the Spotipy module is not included, so we create a virtual environment and install
# whatever we please.
virtualenv --version
if [ $? -ne 0 ] ; then echo "Failed to verify virtualenv, check that it is installed and in your system path"; exit; fi

# Create a virtual environment for python in a folder named 'spotifyVenv'
echo " [ creating virtual environment... ] "

virtualenv spottie

if [ $? -ne 0 ] ; then echo "Failed to create virtual environment, check that it and python are installed and in your system path"; exit; fi

# Download and install the extensions we need with the pip python installer
echo " [ setting up Spotipy... ] "
spottie/bin/pip install Spotipy

if [ $? -ne 0 ] ; then echo "Failed to download and install Spotipy"; exit; fi

# Modify source code until the Spotipy developers get their act together...
echo " [ updating Spotipy for multi-OS support ] "
python SpotipyMod.py

if [ $? -ne 0 ] ; then echo "Failed to update Spotipy, you may have a bad time with the rest of the installation"; exit; fi

# Prompt the user for configuration information
echo " [ creating configuration files  ]"
python create_config.py

if [ $? -ne 0 ] ; then echo "Failed to set up configuration file, please verify that you have ConfigParser in your Python installation"; exit; fi


echo
echo " [ Success ] "
echo
