import os
import testAssembleProfile
import testDB
import testMath
import testPlaylist
import mutatorTest
import configTest

numTests = 0
numPassed = 0

x,y = testAssembleProfile.go()
numTests += x
numPassed += y

x,y = testDB.go()
numTests += x
numPassed += y

x,y = testMath.go()
numTests += x
numPassed += y

x,y = testPlaylist.go()
numTests += x
numPassed += y

x,y = mutatorTest.go()
numTests += x
numPassed += y

x,y = configTest.go()
numTests += x
numPassed += y

print """%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\n%%%%%%%%%% Summary %%%%%%%%%%\n%%%%%%%%%%%%%%%%%%%%%%%%%%%%%"""
print "\n\nTests Issued: %d\nTests Passed: %d\nPercentage: %f\n\n" % (numTests, numPassed, ((100.0*numPassed)/numTests))
