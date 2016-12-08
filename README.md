# 448_Project4
Recommendation system using the Spotify API, team project for software engineering EECS448

##Known Issues:
Our setup is not prepared for users with less than 20 songs in their library.  Users with such narrow preference should seek outside help for their problems.

Our processing of popularity skews results, such that a user with a preference for unpopular songs will rarely be recommended a popular song.  This is included here since the popularity reported by the Spotify API does not match the bounds specified in their documentation.  Instead of varying between 0 and 100, the values returned are greater than zero but apparently unbound above.

Authentication fails intermittently, and makes inappropriate requests for logins.  This appears to be a problem in the Python wrapper for the Spotify API, and will not be resolved because an issue is already open for it on the developer's repository.

The testing suite requires multiple logins, again due to errors in the Spotipy source.
