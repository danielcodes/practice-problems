
# robber problem
# a robber wants to maximize his loot by robbing houses, can't rob two houses in a row

# approach, keep a 2D array one for robbing and one for not robbing
# when not robbing, the value should be the maximum value seen so far
# if robbing it should be the prev non-robbing value added to the current house to be robbed

def robHouses(houses):
	
    n = len(houses)
    
    # create 2D array first
    table = [ [0]*(n+1) for i in range(2) ]
    
    # O(1) space solution
    # prevNo = 0
    # prevYes = 0
    
    # iterate through the houses
    for j in range(1, n+1):
        # row 0 is for not robbing, 1 is for robbing
        table[0][j] = max(table[0][j-1], table[1][j-1])
        table[1][j] = houses[j-1] + table[0][j-1]
        
        # temp = prevNo
        # prevNo = max(prevNo, prevYes)
        # prevYes = houses[j-1] + temp
        # print prevNo, prevYes

    for row in table:
        print row
            
    return max(table[0][n], table[1][n])
	

h = [5, 2, 7, 1, 3, 9]
print h
print 'maximum loot from this sequence of houses\n', robHouses(h)


