
# solve a sudoku puzzle using backtracking
# look for an empty spot and try out all possible values
# if it's valid, recurse. if not, try out all possible 9 values
# if its exhausted, undo last assignment

from math import sqrt

def solveSudokuHelper(i, j, grid):
    # this check is done column by column

    # base case
    if i == len(grid):
        i = 0 # back to top
        j = j+1 # new col
        if j == len(grid[i]):
            return True

    # skip nonEmpty entries
    if grid[i][j] != 0:
        # there was a big bug here, w/o the return
        # it started overwriting values that were already marked
        # such a headache of a problem
        return solveSudokuHelper(i+1, j, grid)

    # attempt all possible values
    for x in range(1, len(grid)+1):
        if isValid(x, i, j, grid):
            grid[i][j] = x
            if solveSudokuHelper(i+1, j, grid):
                return True

    # all values are invalid, backtrack
    grid[i][j] = 0
    return False


def isValid(val, i, j, grid):
    # must check row, col and subgrid
    # row check
    l = len(grid)
    for x in range(l):
        if val == grid[i][x]:
            return False

    # col check
    for y in range(l):
        if val == grid[y][j]:
            return False

    # find which subgrid to check
    # in terms of 0, 1 or 2
    # thinking that the division does not make a difference since
    # the division cuts it down to an int
    subGridL = int(sqrt(l))
    I = i/subGridL
    J = j/subGridL
    for p in range(subGridL):
        for q in range(subGridL):
            if val == grid[subGridL*I + p][subGridL*J + q]:
                return False

    return True


def solveSudoku(grid):
    return solveSudokuHelper(0, 0, grid)

# 0s are blanks
grid = [ [5, 3, 0, 0, 7, 0, 0, 0, 0],
         [6, 0, 0, 1, 9, 5, 0, 0, 0],
         [0, 9, 8, 0, 0, 0, 0, 6, 0],
         [8, 0, 0, 0, 6, 0, 0, 0, 3],
         [4, 0, 0, 8, 0, 3, 0, 0, 1],
         [7, 0, 0, 0, 2, 0, 0, 0, 6],
         [0, 6, 0, 0, 0, 0, 2, 8, 0],
         [0, 0, 0, 4, 1, 9, 0, 0, 5],
         [0, 0, 0, 0, 8, 0, 0, 7, 9]
       ]

print 'the grid before being solved'
for row in grid:
    print row

solveSudoku(grid)
print '\nthe grid after solving'
for row in grid:
    print row


