'''This file is a hack to work around a poor choice made by the Spotipy developer - He used a call
that only works on OSX, forcing PC/Nix users to copy and paste an url from the command line to
complete the initial authorization process.

Credit to Github user sepehr for his quick fix, which has been sitting on the issues page untouched for 6 months...
https://github.com/plamere/spotipy/pull/30
Accessed November 2016
'''

sourceDir = 'spottie/lib64/python2.7/site-packages/spotipy/util.py'
badLine = 'subprocess.call(["open", auth_url])'
tab= "            "
replacement = 'stdout = os.dup(1)\n' + tab + 'stderr = os.dup(2)\n' + tab + 'os.close(1)\n' + tab + 'os.close(2)\n' + tab + 'os.open(os.devnull, os.O_RDWR)\n' + tab + 'webbrowser.open(auth_url, new=1)\n' + tab + 'os.dup2(stdout, 1)\n' + tab + 'os.dup2(stderr, 2)'

original = open(sourceDir, 'r')
origContents = original.read()
original.close()

# find the offending call
index = origContents.find(badLine)

# if it still exists...
if index > 0:
	print "\n[ Modifying util.py to be friendly to PC/Linux... ]"

	# Remove the offending line and splice in a replacement
	newContents = origContents[:index] + replacement + origContents[(index+len(badLine)):]

	# tack on an agnostic web browser library at the top
	index = newContents.find("import spotipy")
	newContents = newContents[:index] + "import webbrowser\n" + newContents[index:]
	try:
		temp = open(sourceDir, 'w')
		temp.write(newContents)
		temp.close()
	except:
		print "\n[ An error occurred while updating the source file.  Attempting to correct it, please run setup again. ]"
		try:
			temp2 = open(sourceDir, 'w')
			temp2.write(origContents)
			temp2.close()
		except:
			print "\n[ Something happened.  Here are the contents of the original file, please replace it manually. ]"
			print origContents
			print
			print
else:
	print "\n[ No need to modify, the script is ready... ]"
