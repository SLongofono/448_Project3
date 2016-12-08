import sys
import REKTUser

#tests:
#zip all?

def testAddData(ru):
        testSong = [['Sufjan Stevens', 'The National'], ['Indie folk', 'Indie Rock'], 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0]
        expectedResult = [['Sufjan Stevens', 'The National'], ['Indie folk', 'Indie Rock'], [1.0], [2.0], [3.0], [4.0], [5.0], [6.0], [7.0], [8.0]]
        
        print "Adding test song into REKTUser's mutators"
        ru.addData(testSong)
        
        print "Searching for new song in REKTUser's addVector data"
        songFound = True
        for i in range(len(ru.addVector)):
            #print ru.addVector[i]()
            #print expectedResult[i]
            
            if ru.addVector[i]() != expectedResult[i]:
                songFound = False
        
        return songFound

def testStdDev(ru):
        print "Calculating standard deviation"
        ru.calculateStandardDeviations()
        return (len(ru.stdDevs) == 8)
    
def testSongDiffs(ru):
        testSongVectors = [[['Sufjan Stevens', 'The National'], ['Indie folk', 'Indie Rock'], 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0]]
        
        print "Calculating song difference vector"
        songDiffs = ru.getSongDifferences(testSongVectors)
        return len(songDiffs[0]) == len(testSongVectors[0])

def go():
        numTests = 3
        numPassed = 0
    
        #create test user
        ru = REKTUser.User(debug=False)
        
        #call sub-tests
        print "\nTesting ability to add song data... "
        test1 = testAddData(ru)
        print "Passed." if test1 else "Failed."
        
        print "\nTesting standard deviation calculation... "
        test2 = testStdDev(ru)
        print "Passed." if test2 else "Failed."
        
        print "\nTesting ability to create song difference vector... "
        test3 = testSongDiffs(ru)
        print "Passed." if test3 else "Failed."
        
        if test1:
            numPassed += 1
        if test2:
            numPassed += 1
        if test3:
            numPassed += 1
        
        #temp test
        
        #end temp
        
        return (numTests, numPassed)

if __name__ == '__main__':
        x, y = go()
       	print "\nNumber of tests: %d\t\tTests Passed: %d\n" % (x,y)

