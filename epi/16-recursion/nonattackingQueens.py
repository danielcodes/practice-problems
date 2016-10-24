
# n non-attacking queen placement in a nxn board
# find all possibilities

# approach is to create arrays that hold column position for valid placements
# so start by picking the first column in the first row, move to the second row
# and look for a valid position, and keep recursing
# if it's not valid, all columns are attempted and nada, we got back in the recursion stack

def findQueenPlacement(n, row, col_placement, result):
	
    # base case, have recursed to the last row 
    if row == n:
        # gotta make a copy cuz, when the list changes from the recursion
        # it affects the list
        validPlacement = list(col_placement)
        result.append(validPlacement)
    else:
        # have to test all columns in a row 
        for col in range(n):
            col_placement.append(col)
            if isValid(col_placement):
                findQueenPlacement(n, row+1, col_placement, result)
            col_placement.pop()


def isValid(col_placement):
	
    # this function needs reviewing, the logic still feels weird
    row_id = len(col_placement) - 1
    for i in range(row_id):
        diff = abs(col_placement[i] - col_placement[row_id])
        if diff == 0 or diff == row_id-i:
            return False
    # no conflicts
    return True


def solveNxNQueens(n):
	
    result = []
    findQueenPlacement(n, 0, [], result)
    return result


n = 4
print 'the placements for non-attacking queens in a {}x{} board is'.format(n, n)
print solveNxNQueens(n)


