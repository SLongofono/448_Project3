import sys
import REKTUser

#tests:
#zip all?

def testAddData(ru):
        testSong = [['Sufjan Stevens', 'The National'], ['Indie folk', 'Indie Rock'], 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0]
        expectedResult = [['Sufjan Stevens', 'The National'], ['Indie folk', 'Indie Rock'], [1.0], [2.0], [3.0], [4.0], [5.0], [6.0], [7.0], [8.0]]
        
        ru.addData(testSong)
        
        songFound = True
        for i in range(len(ru.addVector)):
            #print ru.addVector[i]()
            #print expectedResult[i]
            
            if ru.addVector[i]() != expectedResult[i]:
                songFound = False
                
        return songFound

def testStdDev(ru):
        ru.calculateStandardDeviations()
        return (len(ru.stdDevs) == 8)
    
def testSongDiffs(ru):
        testSongVectors = [[['Sufjan Stevens', 'The National'], ['Indie folk', 'Indie Rock'], 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0]]
        
        songDiffs = ru.getSongDifferences(testSongVectors)
        return len(songDiffs[0]) == len(testSongVectors[0])

def go():
        numTests = 3
        numPassed = 0
    
        #create test user
        ru = REKTUser.User(debug=False)
        
        #call sub-tests
        if testAddData(ru):
            numPassed += 1
        if testStdDev(ru):
            numPassed += 1
        if testSongDiffs(ru):
            numPassed += 1
        
        #temp test
        
        #end temp
        
        return (numTests, numPassed)

if __name__ == '__main__':
        x, y = go()
       	print "\nNumber of tests: %d\t\tTests Passed: %d\n" % (x,y)

