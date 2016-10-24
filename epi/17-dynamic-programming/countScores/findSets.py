
# counting the ways to get a sum given an array of numbers
# ie s = 5, a = [1, 2, 3], given the denominations find how many ways
# are there to make 5

# variation, get the sets, not just the number 

def addNewSets(value, coin, table):
	
    remainder = value - coin
    for s in table[remainder]:
        newSet = list(s)
        newSet.append(coin)
        table[value].append(newSet)
	

def waysToGetNum(s, numbers):
	
    table = {}
    for i in range(0, s+1):
        table[i] = []
            
    table[0].append([])
    # print table
    
    for num in numbers:
        for i in range(num, s+1):
                
            # here, for the given coin, append it to each of the remainder's sets
            # this create the value that we currently want
            addNewSets(i, num, table)
                
    # print table
    return table
	
a = [1, 2, 3]
s = 5

# ways to get 5 counting, 11111, 2111, 221, 311, 32
result = waysToGetNum(s, a)

print 'Given the coins {}, we want to make a sum of {} \n'.format(a, s)

for k, v in result.items():
    print 'the sets to make',k , 'are:'
    print v, '\n'


