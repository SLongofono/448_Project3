# 448_Project4
Recommendation system using the Spotify API, team project for software engineering EECS448

##Getting Started
RTFM. Just kidding, sort of, but really - start with the user manual to get set up.  If you want to play around with the source, most of the heavy lifting is done in the populatePlaylist.py script, and the details of the database schema are laid out in Assemble_profile.py.  Happy hacking.

##Using the Test Suite
After setting up a developer account and running the run.py script as detailed in the user manual, you should be able to run the test suite.  Make sure you have an internet connection, and run the testSuite.py script:
```bash
python testSuite.py
```

##Bug List & Known Issues:
Our setup is not prepared for users with less than 20 songs in their library.  Users with such narrow preference should seek outside help for their problems.

Our processing of popularity skews results, such that a user with a preference for unpopular songs will rarely be recommended a popular song.  This is included here since the popularity reported by the Spotify API does not match the bounds specified in their documentation.  Instead of varying between 0 and 100, the values returned are greater than zero but apparently unbound above.

Authentication fails intermittently, and makes inappropriate requests for logins.  This appears to be a problem in the Python wrapper for the Spotify API, and will not be resolved because an issue is already open for it on the developer's repository.

The testing suite requires multiple logins, again due to errors in the Spotipy source.

Song names, artists, or genres with punctuation cause errors with our database entry, and can cause the Assemble_Profile.py script to fail.  A temporary workaround is in place to strip the name of apostrophes, but other punctuation will still halt execution.
