import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)

import Variance
import math


def testVariance():
	print ("1. Testing Variance")
	weighting = [2,2,2,2,2,2,2,2,2,2]
	test1 = [['artist1', 'artist2', 'artist3'],['genre1', 'genre2', 'genre3'],0,0,0,0,0,0,0,0]
	test2 = [['artist1'],['genre1', 'genre2'],1,2,3,4,5,6,7,8]
	test3 = [['artist1'],['genre1','genre2'],6,7,8,9,2,3,4,5]
	test4 = []
	emptylist = -1

	diffList1 = []
	diffList2 = []

	knownVal1 = [0,0,1,2,3,4,5,6,7,8]
	knownVal2 = [0,0,5,5,5,5,3,3,3,3]


	print "\t A. Variance between a populated list and a list of zeros ..."
	for i in range(len(test1)):
		diffList1.append(Variance.getVariance(test1,test2)[i] -knownVal1[i])

	print "\t B. Variance between 2 populated lists ..."
	for i in range(len(test2)):
		diffList2.append(Variance.getVariance(test3,test2)[i] - knownVal2[i])

	print "\t C. Variance calculated on an empty List ..."
	emptylistValue = Variance.getVariance(test3,test4)

	if emptylistValue == emptylist:
		for i in range (len(diffList1)):
			if ((diffList1[i] or diffList2[i]) > .0000001):
				return False
		return True

def testWeightedDifference():
	print "2. Testing Weighted Difference"
	weighting = [2,2,2,2,2,2,2,2,2,2]
	badWeighting = []
	test1 = [['artist1', 'artist2', 'artist3'],['genre1', 'genre2', 'genre3'],0,0,0,0,0,0,0,0]
	test2 = [['artist1'],['genre1', 'genre2'],1,2,3,4,5,6,7,8]
	test3 = [['artist1'],['genre1', 'genre2'],6,7,8,9,2,3,4,5]
	test4 = []

	diffList1 = []
	diffList2 = []
	diffList3 = []
	knownVal1 = [0,0,2,4,6,8,10,12,14,16]
	knownVal2 = [0,0,10,10,10,10,6,6,6,6]
	emptylistValue = -1

	print "\t A. Weighted Difference between a populated list and a list of zeros ..."
	for i in range(len(test1)):
  		diffList1.append(Variance.getWeightedDifference(test2, test1, weighting)[i] - knownVal1[i])

	print "\t B. Weighted Difference between 2 populated lists ..."
	for i in range(len(test1)):
		diffList2.append(Variance.getWeightedDifference(test3, test2, weighting)[i] - knownVal2[i])

	print "\t C. Testing when Weighting is an empty list ..."
	diffList3 = Variance.getWeightedDifference(test3,test2,badWeighting)

	print "\t D.Testing when one of the lists is an empty list ..."
	emptylist = Variance.getWeightedDifference(test4,test2,weighting)

	if emptylist == emptylistValue:
		for i in range(len(diffList1)):
			if((diffList1[i] or diffList2[i])> .0000001):
				return False
		return True

def testgetNewWeight():
	print "3. Testing getNewWeight"
	badstddevs = []
	stddevs = [1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0]

	knownVal1 = [1, 1, 1, 0.5, 0.333, 0.25, 0.2, 0.167, 0.143, 0.125]
	emptylistValue = -1

	diffList = []

	print "\t A. getNewWeight when stddevs is empty ..."
	emptylist =  Variance.getNewWeight(badstddevs)


	print "\t B. getNewWeight when stddevs is populated ..."
	for i in range(len(knownVal1)):
		diffList.append(Variance.getNewWeight(stddevs)[i] - knownVal1[i])

	if emptylist == emptylistValue:
		for i in range(len(diffList)):
			if(diffList[i] > .0000001):
				return False
	return True


def filter2sigmaTest():
	print("4. Testing Filter2Sigma")
	averages = [[],[],10.0,10.0,10.0,10.0,10.0,10.0,10.0,10.0]
	stddevs = [2.0,2.0,2.0,2.0,2.0,2.0,2.0,2.0]
	knownVal = [1, 1, 1, 0, 0, 0, 0]
	testSongs = [
		[[],[], 10.0,10.0,10.0,10.0,10.0,10.0,10.0,10.0],
		[[],[], 6.0,10.0,10.0,10.0,10.0,10.0,10.0,10.0],
		[[],[], 10.0,10.0,10.0,10.0,10.0,10.0,10.0,14.0],
		[[],[], 5.0,10.0,10.0,10.0,10.0,10.0,10.0,10.0],
		[[],[], 0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0],
		[[],[], 15.0,10.0,10.0,10.0,10.0,10.0,10.0,10.0],
		[[],[], 10.0,10.0,10.0,10.0,10.0,10.0,10.0,15.0],
		]


	val = Variance.filter2Sigma(testSongs, averages, stddevs)
	return val == knownVal


def teststdDev():
	print("5. Testing Standard Deviation")
	stdDev = []
	diffList = []
	listWithRowsAsColumns = [[1,2,3,4,5,6,7,8],
                             [6,1,9,0,5,7,3,4],
                             [5,5,5,5,5,5,5,5],
                             [23,100,1,0,8,9,5,6],
                             [7,5,4,3,2,1,9,6]
                            ]
	listofCalculatedStdDevs = [2.449,3.0,0.0,33.481,2.645]
	for column in listWithRowsAsColumns:
		vals = [x for x in column]
		Nval = len(vals)
		mean = sum(vals)/Nval
		stdDev.append((sum([(x-mean)**2 for x in vals])/(Nval-1))**0.5)
	for i in range(len(listofCalculatedStdDevs)):
		diffList.append(stdDev[i] - listofCalculatedStdDevs[i])

	for i in range(len(diffList)):
		if(diffList[i] > .001):
			return False
	return True
def mathTest():
	numTests = 0
	numPassed = 0
	print "**************************************"
	print "********MATH FUNCTION TESTING*********"
	print "**************************************"
	numTests +=1
	if testVariance():

		print "\t Variance test passed! \n\n"
		numPassed += 1

	numTests +=1
	if testWeightedDifference():

		print "\tWeightedDifference test passed!\n\n"
		numPassed +=1

	numTests +=1
	if testgetNewWeight():

		print "\t getNewWeight test passed!\n\n"
 		numPassed +=1

	numTests +=1
	if (filter2sigmaTest()):

		print "\t f2sigma test passed!\n\n"
		numPassed+=1
	numTests +=1
	if(teststdDev()):

		print "\t Standard Deviation Test Passed!"
        numPassed +=1
	return numTests,numPassed
if __name__ == "__main__":
	x,y = mathTest()
	print "Tests: %d\nTests passed: %d\nPercentage: %f\n\n" % (x,y, (float(y)/x)*100)
