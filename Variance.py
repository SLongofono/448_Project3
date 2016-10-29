import math

## @fn listVariance
#  @brief Check if two lists are disjoint
#  @param in base A list of values representing a set to check against
#  @param in new A list of values to compare with base
#  @return 1 if any members of new are also members of base, 0 otherwise
#  @detail listVariance is essentially checking if the given lists are disjoint.
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


## @fn valueVariance
#  @brief Compute the absolute difference between two numerical values
#  @param in base A numerical type feature from the user profile vector
#  @param in new A numerical type feature from a new song vector
#  @return A float value representing the absolute difference between base and new
#  @detail This method compares two values to compute the positive difference (delta)
#	from the user profile vector feature described by base.
def valueVariance(base, new):
    return math.fabs(base-new)


## @var compareVec
#  @brief A list of functions to compute variance of two vectors
#  @detail compareVec holds references to functions to be applied when evaluating the
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


## @fn getVariance
#  @brief Apply the functions in compareVec to the values in base, new
#  @param in base The user profile vector
#  @param in new a list of features to compare against the user vector
#  @return A list of quantified differences for each feature
#  @detail Each of the functions in compareVec is called using the 
#	   Cartesian product of base and new.  The resultant list of
#	   differences is returned.
def getVariance(base, new):
	results = []
	for i in range(len(base)):
		results.append(compareVec[i](base[i], new[i]))

	return results



if __name__ == '__main__':
	print "No need to run this directly"
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
