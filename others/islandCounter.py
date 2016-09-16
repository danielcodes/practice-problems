
# Given a 2D matrix of 1s and 0s, count the islands
# island are defined by a group of 1s adjacent to each other (4 ways), can also be singular

from collections import deque

a = [[0, 1, 0, 1, 0],
     [0, 0, 1, 1, 1],
     [1, 0, 0, 1, 0],
     [0, 1, 1, 0, 0],
     [1, 0, 1, 0, 1]]

print 'the matrix is'

def printGrid(arr):
    for r in arr:
        print r

def islandCounter(arr):

    islands = 0
    # these are set to 5 and 5 respectively
    row = len(arr)
    col = len(arr[0])

    for i in range(row):
        for j in range(col):

            if arr[i][j] == 1:
                markIsland(arr, i, j, row, col)
                islands += 1

    print 'the # of islands in this matrix is', islands
    return islands

def markIsland(arr, i, j, row, col):

    # use a queue (bfs) to expand on adjacent ones
    q = deque()
    q.append((i, j))

    print 'checking islands for {} {}'.format(i, j)

    # if there are still items to check
    while q:
        x, y = q.popleft()
        
        # expand
        if arr[x][y] == 1:
            arr[x][y] += 1

            pushIfValid(arr, x+1, y, row, col, q)
            pushIfValid(arr, x-1, y, row, col, q)
            pushIfValid(arr, x, y+1, row, col, q)
            pushIfValid(arr, x, y-1, row, col, q)

    print 'after finding islands'
    printGrid(arr)


def pushIfValid(arr, i, j, row, col, q):

    # push values into the queue
    if (0 <= i and i < row) and (0 <= j and j < col):
        q.append((i,j))

printGrid(a)
islandCounter(a)


