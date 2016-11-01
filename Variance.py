##@file Variance.py
#	@brief This file defines helper functions for evaluating and processing differences between song vectors
#
import math


##@var compareVec
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


##@fn getVariance
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


##@fn listVariance
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


##@fn valueVariance
#  @brief Compute the absolute difference between two numerical values
#  @param base A numerical type feature from the user profile vector
#  @param new A numerical type feature from a new song vector
#  @return A float value representing the absolute difference between base and new
#  @details This method compares two values to compute the positive difference (delta)
#	from the user profile vector feature described by base.
def valueVariance(base, new):
    return math.fabs(base-new)


# Debugging and ad-hoc testing
if __name__ == '__main__':
	print "No need to run this directly, use getVariance() and pass in the user profile vector and the vector to be compared."
	test1 = [['artist1', 'artist2', 'artist3'],['genre1', 'genre2', 'genre3'],0,0,0,0,0,0,0,0]
	test2 = [['artist1'],['genre1', 'genre2'],1,2,3,4,5,6,7,8]
	print getVariance(test1, test2)
'''     The expected difference of the above should be:
	0.33333333
	0.66666666
	1
	2
	3
	4
	5
	6
	7
'''
