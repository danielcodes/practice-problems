
# find how ways are there to traverse a 2D array, from top left to bottom right
# can only move right or down

# top down recursive solution, to get to (i, j) we need to sum up ways 
# to get to (i-1, j) the left and (i, j-1) the top

def createMatrix(n, m):
	
    matrix = []
    for i in range(n):
        matrix.append( [0]*m )
    
    return matrix
	
	
def findWays(i, j, grid):
	
    # only one way to get to the origin
    if i == 0 and j == 0:
        return 1 
    
    # has not been visited yet
    if grid[i][j] == 0:
            
        waysTop = 0
        waysLeft = 0
        
        # recursive calls to top and left
        if i != 0:
            waysTop = findWays(i-1, j, grid)
        
        if j != 0:
            waysLeft = findWays(i, j-1, grid)
                
        grid[i][j] = waysTop + waysLeft
    
    return grid[i][j]
			
	
n = 4
m = 4

a = createMatrix(n, m)
print 'answer', findWays(n-1, m-1, a)

for r in a:
    print r



