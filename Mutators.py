## @file Mutators.py
# Mutators
# @brief A collection of functions used to incorporate new feature values into existing average values
#

## Generic_Mutator
# @brief Mutator functions define functions which track a list of values across calls
# @param vals An implicit list of values which this function will store dynamically.
#                Should never be passed in explicitly.
# @param newVal An optional list of values or value to be tracked in this functions
#                  vals list.
# @param debug A Boolean indicating whether the state before/after should be
#                 printed for this function's vals
# @return The list vals, containing all pertinent values which were added in the
#         current session
# @detail The various mutator functions allow a state to be tracked across calls.
#         Each function will check if a newVal parameter is present, and if so the
#         parameter will be appended to the vals list.  For those functions designed
#         to tracks multiple lists, only the unique elements of newVal will be added
#         to the vals list.
#
def Generic_Mutator(vals=[], newVal=None, debug=False):
    return

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
    return vals

def acousticnessMutator(vals=[], newVal=None, debug=False):
    if newVal:
        if debug:
            print 'Old values: ', vals
            vals.append(newVal)
            print 'New values: ', vals
        else:
            vals.append(newVal)
    return vals

def danceabilityMutator(vals=[], newVal=None, debug=False):
    if newVal:
        if debug:
            print 'Old values: ', vals
            vals.append(newVal)
            print 'New values: ', vals
        else:
            vals.append(newVal)
    return vals

def energyMutator(vals=[], newVal=None, debug=False):
    if newVal:
        if debug:
            print 'Old values: ', vals
            vals.append(newVal)
            print 'New values: ', vals
        else:
            vals.append(newVal)
    return vals

def instrumentalnessMutator(vals=[], newVal=None, debug=False):
    if newVal:
        if debug:
            print 'Old values: ', vals
            vals.append(newVal)
            print 'New values: ', vals
        else:
            vals.append(newVal)
    return vals

def keyMutator(vals=[], newVal=None, debug=False):
    if newVal:
        if debug:
            print 'Old values: ', vals
            vals.append(newVal)
            print 'New values: ', vals
        else:
            vals.append(newVal)
    return vals

def livenessMutator(vals=[], newVal=None, debug=False):
    if newVal:
        if debug:
            print 'Old values: ', vals
            vals.append(newVal)
            print 'New values: ', vals
        else:
            vals.append(newVal)
    return vals

def valenceMutator(vals=[], newVal=None, debug=False):
    if newVal:
        if debug:
            print 'Old values: ', vals
            vals.append(newVal)
            print 'New values: ', vals
        else:
            vals.append(newVal)
    return vals
