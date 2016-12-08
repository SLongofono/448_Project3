import sys
import REKTUser

#tests:
#add
#get song differences?
#process profile?
#save status?
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

def go():
        numTests = 1
        numPassed = 0
    
        #create test user
        rektUser = REKTUser.User(debug=False)
        
        #call sub-tests
        if testAddData(rektUser):
            numPassed += 1
        
        
        return (numTests, numPassed)

if __name__ == '__main__':
        x, y = go()
       	print "\nNumber of tests: %d\t\tTests Passed: %d\n" % (x,y)

