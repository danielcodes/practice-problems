
# print a NxN matrix in spiral order
# approach is to create uniform for loops
# iteration occurs for every n-1 items in each of the 4 directions
# use an offset variable to slowly exaust the smaller grids
# edge case on odd grids

def createMatrix(n):
    a = []
    for i in range(1, n*n, n):
        row = []
        for j in range(n):
            row.append(i+j)
        a.append(row)

    return a

def createSpiral(grid):
    
    result = []
    length = len(grid)
    offset = 0
    
    while offset <= length-offset-1:
        
        # check for an odd grid and return
        if offset == length-offset-1:
            result.append(grid[offset][offset])
            return result
        
        # otherwise just do the uniform iterations
        # n-1 each time
        for i in range(offset, length-offset-1):
            result.append(grid[offset][i])
        
        for j in range(offset, length-offset-1):
            result.append(grid[j][length-offset-1])
        
        for k in range(length-offset-1, offset, -1):
            result.append(grid[length-offset-1][k])
        
        for h in range(length-offset-1, offset, -1):
            result.append(grid[h][offset])
            
        offset += 1
            
    return result


a = createMatrix(3)
print 'a 3x3 matrix and its spiral form'
print a
print createSpiral(a)

print ''

b = createMatrix(4)
print 'a 4x4 matrix and its spiral form'
print b
print createSpiral(b)


