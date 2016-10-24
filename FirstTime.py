# Run me once after running Assemble_Profile.py to gather a user's first 200 songs.
# You may want to create a dummy

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
