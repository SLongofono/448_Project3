##@file Mutators.py
# @brief A collection of functions used to incorporate new feature values into existing average values
#

##@fn Generic_Mutator
# @brief Mutator functions define functions which track a list of values across calls
# @param in vals An implicit list of values which this function will store dynamically.
#                Should never be passed in explicitly.
# @param in newVal An optional list of values or value to be tracked in this functions
#                  vals list.
# @param in debug A Boolean indicating whether the state before/after should be
#                 printed for this function's vals
# @return The list vals, containing all pertinent values which were added in the
#         current session
# @detail The various mutator functions allow a state to be tracked across calls.
#         Each function will check if a newVal parameter is present, and if so the
#         parameter will be appended to the vals list.  For those functions designed
#         to tracks multiple lists, only the unique elements of newVal will be added
#         to the vals list.
#

def getUniques(l1, l2):
    result = []
    for i in l2:
        if not i in l1:
            result.append(i)

    return result


def artistMutator(vals=[], newVal=None, debug=False):
    if newVal:
        if debug:
            print 'Old values: ', vals
            temp = getUniques(vals, newVal)
            vals += temp
            print 'New values: ', vals
        else:
            vals += getUniques(vals, newVal)
    return vals

def genreMutator(vals=[], newVal=None, debug=False):
    if newVal:
        if debug:
            print 'Old values: ', vals
            temp = getUniques(vals, newVal)
            vals += temp
            print 'New values: ', vals
        else:
            vals += getUniques(vals, newVal)
    return vals

def popularityMutator(vals=[], newVal=None, debug=False):
    if newVal:
        if debug:
            print 'Old values: ', vals
            vals.append(newVal)
            print 'New values: ', vals
        else:
            vals.append(newVal)
    return sum(vals)/len(vals) if len(vals) > 0 else 0

def acousticnessMutator(vals=[], newVal=None, debug=False):
    if newVal:
        if debug:
            print 'Old values: ', vals
            vals.append(newVal)
            print 'New values: ', vals
        else:
            vals.append(newVal)
    return sum(vals)/len(vals) if len(vals) > 0 else 0

def danceabilityMutator(vals=[], newVal=None, debug=False):
    if newVal:
        if debug:
            print 'Old values: ', vals
            vals.append(newVal)
            print 'New values: ', vals
        else:
            vals.append(newVal)
    return sum(vals)/len(vals) if len(vals) > 0 else 0

def energyMutator(vals=[], newVal=None, debug=False):
    if newVal:
        if debug:
            print 'Old values: ', vals
            vals.append(newVal)
            print 'New values: ', vals
        else:
            vals.append(newVal)
    return sum(vals)/len(vals) if len(vals) > 0 else 0

def instrumentalnessMutator(vals=[], newVal=None, debug=False):
    if newVal:
        if debug:
            print 'Old values: ', vals
            vals.append(newVal)
            print 'New values: ', vals
        else:
            vals.append(newVal)
    return sum(vals)/len(vals) if len(vals) > 0 else 0

def keyMutator(vals=[], newVal=None, debug=False):
    if newVal:
        if debug:
            print 'Old values: ', vals
            vals.append(newVal)
            print 'New values: ', vals
        else:
            vals.append(newVal)
    return sum(vals)/len(vals) if len(vals) > 0 else 0

def livenessMutator(vals=[], newVal=None, debug=False):
    if newVal:
        if debug:
            print 'Old values: ', vals
            vals.append(newVal)
            print 'New values: ', vals
        else:
            vals.append(newVal)
    return sum(vals)/len(vals) if len(vals) > 0 else 0

def valenceMutator(vals=[], newVal=None, debug=False):
    if newVal:
        if debug:
            print 'Old values: ', vals
            vals.append(newVal)
            print 'New values: ', vals
        else:
            vals.append(newVal)
    return sum(vals)/len(vals) if len(vals) > 0 else 0
