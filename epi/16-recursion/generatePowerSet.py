
# generate the power set, which is all possible subarrays and includes
# the empty set and the set itself
# approach, a recursive backtracking approach
# ie. [1, 2, 3]
# the recursive steps is as follows, take one and don't take one
# and compute the power set for those smaller arrays

def generatePSHelper(values, to_select, selected, powerSet):

    # base case
    if to_select == len(values):
        result = list(selected)
        powerSet.append(result)
        return
    
    # recursive cases, with and without the char
    selected.append(values[to_select])
    generatePSHelper(values, to_select+1, selected, powerSet)
    selected.pop()
    generatePSHelper(values, to_select+1, selected, powerSet)


def generatePowerSet(values):

    powerSet = []
    generatePSHelper(values, 0, [], powerSet)
    return powerSet

values = [1, 2, 3]
print 'the powerset generated from {} is:\n{}'.format(values, generatePowerSet(values))


