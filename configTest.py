#import create_config
import os

def configTest():
    print "Testing create_config Function ..."
    if os.path.isfile(".rektconfig.txt"):
        print "Test Passed -- File successfully opened"
        return True
    else:
        print "Test Failed -- Verify that create_config script has been ran"
        return False


def go():
    print "**************************************"
    print "********create_config TESTING*********"
    print "**************************************"
    numTests = 1
    numPassed = 0
    if configTest():
        numPassed +=1

    print "Tests: %d\nTests passed: %d\nPercentage: %f\n\n" % (numTests,numPassed, (float(numPassed)/numTests)*100)
    return numTests, numPassed

if __name__ == "__main__":
	x,y = go()
	print "Tests: %d\nTests passed: %d\nPercentage: %f\n\n" % (x,y, (float(y)/x)*100)
