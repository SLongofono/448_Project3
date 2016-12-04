import Mutators

def  getUniquesTest():
    print "Testing getUniques Function..."
    knownUniques = [0,99,8000]
    l1 = [1,2,3,4,5,6,7,8,9]
    l2 = [0,1,2,3,4,99,5,6,7,8,9,8000]
    return Mutators.getUniques(l1,l2) == knownUniques

def artistMutatorTest():
    print "Testing ArtistMutator Function"
    values = ['a','b','c']
    newValues = ['a','b','c','d']
    newValueswithNorepeats = ['a','b','c']
    return (Mutators.artistMutator(values,newValues) == newValues and (Mutators.artistMutator(values,newValueswithNorepeats)==values))

def popularityMutatorTest():
    print "Testing PopularityMutator Function"
    values = [1,2,3]
    newValues = [1,2,3,1]
    return (Mutators.popularityMutator(values,1) == newValues)

def acousticnessMutatorTest():
    print "Testing AcousticnessMutator Function"
    values = [1,2,3]
    newValues = [1,2,3,1]
    return (Mutators.acousticnessMutator(values,1) == newValues)

def valenceMutatorTest():
    print"Testing ValenceMutator Function"
    values = [1,2,3]
    newValues = [1,2,3,1]
    return (Mutators.valenceMutator(values,1) == newValues)

def danceabilityMutatorTest():
    print"Testing danceabilityMutator Function"
    values = [1,2,3]
    newValues = [1,2,3,1]
    return (Mutators.danceabilityMutator(values,1) == newValues)

def energyMutatorTest():
    print"Testing energyMutator Function"
    values = [1,2,3]
    newValues = [1,2,3,1]
    return (Mutators.energyMutator(values,1) == newValues)

def instrumentalnessMutatorTest():
    print"Testing instrumentatlnessMutator Function"
    values = [1,2,3]
    newValues = [1,2,3,1]
    return (Mutators.instrumentalnessMutator(values,1) == newValues)

def keyMutatorTest():
    print"Testing keyMutator Function"
    values = [1,2,3]
    newValues = [1,2,3,1]
    return (Mutators.keyMutator(values,1) == newValues)

def livenessMutatorTest():
    print"Testing livenessMutator Function"
    values = [1,2,3]
    newValues = [1,2,3,1]
    return (Mutators.livenessMutator(values,1) == newValues)

def MutatorTest():
    print "**************************************"
    print "********MUTATOR FUNCTION TESTING******"
    print "**************************************"
    numTests = 0
    numPassed = 0
    numTests +=1
    if getUniquesTest():
        print "\t getUniques Test Passed"
        numPassed += 1

    numTests += 1
    if artistMutatorTest():
        print "\t artistMutator Test Passed "
        numPassed += 1

    numTests += 1
    if popularityMutatorTest():
        print "\t popularityMutator Test Passed "
        numPassed += 1

    numTests += 1
    if acousticnessMutatorTest():
        print "\t acousticnessMutator Test Passed "
        numPassed += 1

    numTests += 1
    if danceabilityMutatorTest():
        print "\t danceabilityMutator Test Passed "
        numPassed += 1

    numTests += 1
    if keyMutatorTest():
        print "\t keyMutator Test Passed "
        numPassed += 1

    numTests += 1
    if energyMutatorTest():
        print "\t acousticnessMutator Test Passed "
        numPassed += 1

    numTests += 1
    if valenceMutatorTest():
        print "\t valenceMutator Test Passed "
        numPassed += 1

    numTests += 1
    if instrumentalnessMutatorTest():
        print "\t instrumentalnessMutator Test Passed "
        numPassed += 1

    numTests += 1
    if livenessMutatorTest():
        print "\t livenessMutator Test Passed "
        numPassed += 1

    return numTests, numPassed
if __name__ == "__main__":
	x,y = MutatorTest()
	print "Tests: %d\nTests passed: %d\nPercentage: %f\n\n" % (x,y, (float(y)/x)*100)
