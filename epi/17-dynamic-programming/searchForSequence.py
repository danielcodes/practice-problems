
# search whether a sequence in a 2D array, can only move up, down, left and right
# approach, visit all values and recurse on it
# base case, the sequence has been found, the (x, y) is out of bounds or already seen
# otherwise, to go forward, meet 2 conditions, the value must match next needed value
# and one of the 4 possible recursize calls has to return true
# return value is a bool, not the sequence

def findSequence(grid, seq):
    
    # keeping the seen tuple values in a set
    prevSeen = set()
    
    # question here is, once it finds a solution, does it exit out?
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            # find and get out
            # print 'recursing on', i, j
            if findSequenceHelper(grid, i, j, seq, 0, prevSeen):
                return True
    
    # seq not found
    return False


def findSequenceHelper(grid, i, j, seq, offset, prevSeen):

    # 2 base cases
    # offset has met length
    if offset == len(seq):
        return True

    # out of bounds or already seen
    if (i < 0 or i >= len(grid)) or (j < 0 or j >= len(grid[0])) or ((i, j) in prevSeen):
        return False

    # has to match and 4 recursive steps
    if grid[i][j] == seq[offset] and (
        findSequenceHelper(grid, i+1, j, seq, offset+1, prevSeen) or
        findSequenceHelper(grid, i-1, j, seq, offset+1, prevSeen) or
        findSequenceHelper(grid, i, j+1, seq, offset+1, prevSeen) or
        findSequenceHelper(grid, i, j-1, seq, offset+1, prevSeen)
        ):
        # print 'coming back from', i, j, grid[i][j]
        return True

    # backtrack
    prevSeen.add((i, j))
    return False


if __name__ == '__main__':

    grid = [[1, 2, 3],
            [3, 4, 5],
            [5, 6, 7]]
    # seq = [1, 3, 4, 6]
    seq = [1, 2, 3, 4]

    for r in grid:
        print r

    print 'sequence to find is', seq
    print 'is seq in found in grid?', findSequence(grid, seq)


