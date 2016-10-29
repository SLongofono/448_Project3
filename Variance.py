import math

def listVariance(base, new):
    for i in new:
        if i in base:
            return 0
    return 1

def valueVariance(base, new):
    return math.fabs(base-new)


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

def getVariance(base, new):
	results = []
	for i in range(len(base)):
		# selectively map our operators based on input type
		if type(base[i]) == list:
			results.append(compareVec[i](base[i], new[i]))
		else:
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
