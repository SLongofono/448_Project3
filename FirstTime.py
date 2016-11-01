##@file FirstTime.py
# @brief Parses a user's local song database and assembles a user profile vector.  Second step of
#        setting up a user profile
# @details This file is run after assembling a database of the user's songs, in order to establish
#         a profile vector for the user.  The profile vector is composed of the average value for
#         numerical features, and two lists representing all the artists and all the genres among
#         a user's set of songs.
# @instructions Run me once after running Assemble_Profile.py to gather a user's first 1000 songs.

import REKTUser

# Create a dummy start profile
x = open('userprofile.txt', 'w')
x.write('{{Bob Marley}}\n{{Death Pop,,Icelandic glam-folk,,}}\n1.0\n1.0\n1.0\n1.0\n1.0\n1.0\n1.0\n1.0')
x.close()

myUser = REKTUser.User(debug=True)
newVectors = []

# Extract lines from file
x = open('SongVectors.txt','r')
labels = x.readline().split('###')
lines = []
for line in x:
    lines.append(line.split('###')[:-1])
x.close()

# Parse lines
for entry in lines:
    newVec = []
    # parse and load artists
    newVec.append(entry[0][2:-2].split(',,'))
    print "Artists: ", newVec[0]

    # parse and load genres
    newVec.append(entry[1][2:-2].split(',,'))
    print "Genres: ", newVec[1]

    print "Others: ", entry[2:]

    # parse and load everything else
    for i in range(2, len(entry)):
        newVec.append(float(entry[i]))

    newVectors.append(newVec)

print "Done gathering vectors..."

# incorporate each into profile
for newVec in newVectors:
    myUser.addData(newVec)

print "Done incorporating vectors into profile..."

myUser.saveStatus()

print "User profile saved..."

myUser.prettyPrintProfile()
