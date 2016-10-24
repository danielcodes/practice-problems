
# generate all possible permutations of an array
# ie. [a, b, c] -> [[a,b,c], [a,c,b], [b,a,c], [b,c,a], [c,b,a], [c,a,b]]
# approach, use a backtracking algorithm, the idea is to hold the first value
# and find all permutations with the rest
# this is repeated for all possible chars by swapping the first value
# with every other character

def generatePerm(idx, values, result):

    if idx == len(values)-1:
        # can't pass values cuz the reference changes back
        # so gotta create a snapshot and save that
        copy = list(values)
        result.append(copy) 
        return

    # start backtrack
    # iteration start at the index you start at
    for i in range(idx, len(values)):
        values[idx], values[i] = values[i], values[idx]
        generatePerm(idx+1, values, result)
        values[idx], values[i] = values[i], values[idx]


def getPermutations(values):

    result = []
    generatePerm(0, values, result)
    return result


a = ['a', 'b', 'c']    
print 'the permutations for {} are:\n{}'.format(a, getPermutations(a)), '\n'

b = [1, 2, 3, 4]    
print 'the permutations for {} are:\n{}'.format(b, getPermutations(b))


