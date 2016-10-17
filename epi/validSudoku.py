
# check whether a partially filled sudoku grid is valid
# no repeated numbers in rows, cols and the 3x3 sub grids
# goal is to write clean code 

def hasDuplicates(grid, row_start, row_end, col_start, col_end):
	
    # use a list to keep track of seen values
    isPresent = [False]*(len(grid)+1)
    for i in range(row_start, row_end):
        for j in range(col_start, col_end):
            if grid[i][j] != 0 and isPresent[grid[i][j]] == True:
                return True
            isPresent[grid[i][j]] = True
    
    return False


def isValidSudoku(grid):
	
    length = len(grid)
    # check rows
    for i in range(0, length):
        if hasDuplicates(grid, i, i+1, 0, length):
            return False

    # check cols
    for j in range(0, length):
        if hasDuplicates(grid, 0, length, j, j+1):
            return False
    
    # check subgrids
    subLength = length / 3 
    for m in range(subLength):
        for n in range(subLength):
            # print m*subLength, (m+1)*subLength, n*subLength, (n+1)*subLength
            if hasDuplicates(grid, m*subLength, (m+1)*subLength, n*subLength, (n+1)*subLength):
                return False
                                                
    return True


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

for row in grid:
    print row
	

print '\nis the sudoku grid valid?', isValidSudoku(grid), '\n'

print 'changing last value of the top row to'
grid[0][-1] = 5
print grid[0]

print '\nis the sudoku grid valid?', isValidSudoku(grid)


