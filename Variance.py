##@file Variance
# Variance
#	@brief This file defines helper functions for evaluating and processing differences between song vectors
#
import math


## getNewWeight
# @brief Create a relative weight vector using standard deviations of features
# @param stddevs A list of the standard deviations for each numerical feature
# @return A relative weight vector of length 10
# @details This method uses a list of standard deviations to determine which of
#	the features is the most specific, i.e. which has the smalles standard
#	deviation.  This is used in a scaling factor to determine the relative
#	weight of each feature, as calculated by the minimum standard deviation
#	divided by the ith standard deviation.  Assumes that the first two
#	entries in the resultant weighting vector are binary (always weighted
#	at unity)
def getNewWeight(stddevs):
	newWeight = [1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0]

	# Find minimum spread about mean
	minSigma = 100
	for i in stddevs:
		if i < minSigma:
			minSigma = i

	# normalize to this spread in a scaling vector
	# Skip first two, artist and genre have binary weight
	for i in range(len(stddevs)):
		newWeight[i+2] *= (minSigma/stddevs[i])

	return newWeight


## getVariance
#  @brief Apply the functions in compareVec to the values in base, new
#  @param base The user profile vector
#  @param new a list of features to compare against the user vector
#  @return A list of quantified differences for each feature
#  @details Each of the functions in compareVec is called using the
#	   Cartesian product of base and new.  The resultant list of
#	   differences is returned.
def getVariance(base, new):
	results = []
	for i in range(len(base)):
		results.append(compareVec[i](base[i], new[i]))

	return results


## getWeightedDifference
#  @brief Computes the vector difference and applies weighting to song vectors
#  @param base The user profile vector
#  @param new a list of features to compare against the user vector
#  @param weighting a list of numeric weights associated with each feature
#  @return A list of weighted, quantified differences for each feature
#  @details This is a convenience function for getting a weighted difference
#	of any two songs vectors.  getVariance is called on the two song vectors
#	to yield a list of 10 numbers representing the difference, and then the
#	weighting vector is applied to scale each difference element.
def getWeightedDifference(new, base, weighting):
	return weight(getVariance(base, new), weighting)


## filter2Sigma
# @brief generates a binary filtering list with which to filter a list of songs
# @param songVectors
# @param songVectors
# @param songVectors
# @return A list of integers representing songs that meet the criterion (1) or do not (0)
# @details This method applies an initial filtering of songs which fall outside of two
#	standard deviations from the mean value of any feature.  This will be used as a
#	part of the recommendation process to weed out songs that are drastically different
#	from anything the user has liked in the past.  The resultant vector will be an ordered
#	filter to apply upstream, to a list of song objects which includes the spotify track ID.
def filter2Sigma(songVectors, averages, stddevs):
	results = []
	for song in songVectors:
		rejected = False
		for i in range(len(stddevs)):
			if math.fabs(song[i+2]-averages[i+2]) > (2*stddevs[i]):
				rejected = True
				break
		if not rejected:
			results.append(1)
		else:
			results.append(0)
	return results


##  listVariance
#  @brief Check if two lists are disjoint
#  @param base A list of values representing a set to check against
#  @param new A list of values to compare with base
#  @return 1 if any members of new are also members of base, 0 otherwise
#  @details listVariance is essentially checking if the given lists are disjoint.
#	This method is used to check list features such as artists or genres,
#	the idea being that there is zero difference from a user profile if the
#	new song has any list elements which are in the user profile list.  The
#	weight of this difference is determined elsewhere, here we just want a
#	binary result.
#
def listVariance(base, new):
    for i in new:
        if i in base:
            return 0
    return 1


##  valueVariance
#  @brief Compute the absolute difference between two numerical values
#  @param base A numerical type feature from the user profile vector
#  @param new A numerical type feature from a new song vector
#  @return A float value representing the absolute difference between base and new
#  @details This method compares two values to compute the positive difference (delta)
#	from the user profile vector feature described by base.
def valueVariance(base, new):
	if new != None:
		return math.fabs(base-new)
	else:
		return 0

## weight
# @brief Apply weighting to a song vector
# @param diffVec a song difference vector to be weighted
# @param weightVec a feature weighting vector
# @return a weight song difference vector
# @details This method applies the weighting vector to the difference vector by performing
#	a piecewise multiplication.  This method should only be applied to difference vectors,
#	as a weighting vector will have 10 numeric values but a song vector will only have 8.
def weight(diffVec, weightVec):
	return [x*y for x,y in zip(diffVec,weightVec)]


# @var compareVec
#  @brief A list of functions to compute variance of two vectors
#  @details compareVec holds references to functions to be applied when evaluating the
#	feature-by-feature difference between two feature vectors.
#
compareVec = 	[
		listVariance,
		listVariance,
		valueVariance,
		valueVariance,
		valueVariance,
		valueVariance,
		valueVariance,
		valueVariance,
		valueVariance,
		valueVariance
		]


# Debugging and ad-hoc testing
if __name__ == '__main__':

	weighting = [2,2,2,2,2,2,2,2,2,2]
	print "No need to run this directly, use getVariance() and pass in the user profile vector and the vector to be compared."
	test1 = [['artist1', 'artist2', 'artist3'],['genre1', 'genre2', 'genre3'],0,0,0,0,0,0,0,0]
	test2 = [['artist1'],['genre1', 'genre2'],1,2,3,4,5,6,7,8]
	print getVariance(test1, test2)
	#The expected difference of the above should be: [0,0,1,2,3,4,5,6,7]

#	print weight(getVariance(test1, test2), weighting)
	print getWeightedDifference(test2, test1, weighting)
	#The expected weighted difference of the above should be: [0,0,2,4,6,8,10,12,14]

	stddevs = [1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0]
	print getNewWeight(stddevs)
	# should produce [1, 1, 1, 0.5, 0.33, 0.25, 0.2, 0.166, 0.143, 0.125]

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

	print filter2Sigma(testSongs, averages, stddevs)
	#Expecting [1,1,1,0,0,0,0]
