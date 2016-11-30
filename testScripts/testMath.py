import math
import Variance

def testVariance():
    	weighting = [2,2,2,2,2,2,2,2,2,2]
    	print "No need to run this directly, use getVariance() and pass in the user profile vector and the vector to be compared."
    	test1 = [['artist1', 'artist2', 'artist3'],['genre1', 'genre2', 'genre3'],0,0,0,0,0,0,0,0]
    	test2 = [['artist1'],['genre1', 'genre2'],1,2,3,4,5,6,7,8]
    	print getVariance(test1, test2)
    	#The expected difference of the above should be: [0,0,1,2,3,4,5,6,7]
def testWeightedDifference():
    	return getWeightedDifference(test2, test1, weighting) == [0,0,2,4,6,8,10,12,14]
    	#The expected weighted difference of the above should be: [0,0,2,4,6,8,10,12,14]
def testgetNewWeight():
    	stddevs = [1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0]
    	return getNewWeight(stddevs) == [1, 1, 1, 0.5, 0.33, 0.25, 0.2, 0.166, 0.143, 0.125]
    	# should produce [1, 1, 1, 0.5, 0.33, 0.25, 0.2, 0.166, 0.143, 0.125]
def filter2sigmaTest():
    	averages = [10.0,10.0,10.0,10.0,10.0,10.0,10.0,10.0]
    	stddevs = [2.0,2.0,2.0,2.0,2.0,2.0,2.0,2.0]
    	testSongs = [
    		[10.0,10.0,10.0,10.0,10.0,10.0,10.0,10.0],
    		[6.0,10.0,10.0,10.0,10.0,10.0,10.0,10.0],
    		[10.0,10.0,10.0,10.0,10.0,10.0,10.0,14.0],
    		[5.0,10.0,10.0,10.0,10.0,10.0,10.0,10.0],
    		[0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0],
    		[15.0,10.0,10.0,10.0,10.0,10.0,10.0,10.0],
    		[10.0,10.0,10.0,10.0,10.0,10.0,10.0,15.0],
    		]
        return filter2Sigma(testSongs, averages, stddevs) == [1,1,1,0,0,0,0]
def teststdDev():
    listWithRowsAsColumns = [[1,2,3,4,5,6,7,8],
                             [6,1,9,0,5,7,3,4],
                             [5,5,5,5,5,5,5,5],
                             [23,100,1,0,8,9,5,6],
                             [7,5,4,3,2,1,9,6]
                            ]
    listofCalculatedStdDevs = [2.44949,3.02076,0,33.48347,2.66927]
    
print
