
# finding the minimum number of coins that sum up to a value
# approach, bottom up table

def findMinCoins(coins, target):
	
    table = [ float('infinity') for i in range(target+1) ]
    table[0] = 0
    
    print [ i for i in range(target+1)]
    print table
    
    for coin in coins:
        # iterate over each value up to target
        for i in range(coin, target+1):
                
            # if we take the coin, we need to find the coins needed to get the remainder
            leftOver = table[i-coin]
            
            # make sure that the remainder can be build and it is less than the current
            # number of coins to make up that value
            if leftOver != float('infinity') and leftOver + 1 < table[i]:
                table[i] = leftOver + 1
        print table
            
    return table[target]
	
	
coins = [2, 3, 5]
target = 7
result = findMinCoins(coins, target)
print 'Given the denominations {}, the min coins needed to get {} is {}\n'.format(coins, target, result)

coins = [1, 3, 5]
target = 11
result = findMinCoins(coins, target)
print 'Given the denominations {}, the min coins needed to get {} is {}'.format(coins, target, result)


