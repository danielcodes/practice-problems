
# knapsack problem, clocks have a weight and value
# given a knapsack with weight k, find a way to maximize the value
# from the clocks that can be stolen

# approach, is to build a table bottom up
# use the items as rows and the weights as columns
# to fill in the a value table[i][j], 2 options
# max btw itemValue + table[item-1][weight - itemWeight] and table[item-1][weight]

# O(nw) time
# O(nw) space

def clockLoot(clocks, bagWeight):

    table = [[0]*(bagWeight+1) for i in range(len(clocks)+1)]
    numClocks = len(clocks)

    print '\nbuilding up the table'
    for row in table:
        print row

    # has to write one row below
    for idx, (weight, value) in enumerate(clocks):
        weightWithItem = 0
        for w in range(bagWeight+1):

            if weight <= w:
                weightWithItem = value + table[idx][w-weight]
            optValue = max(weightWithItem, table[idx][w])
            # on wrie up, gotta access one below
            table[idx+1][w] = optValue
    
    print '\nafter filling in'
    for row in table:
        print row

    return table[numClocks][bagWeight]


# (weight, value)
bagWeight = 5
clocks = [(5, 60), (3, 50), (4, 70), (2, 30)]
print 'the clocks in the store are', clocks
result = clockLoot(clocks, bagWeight)
print '\nthe maximum loot with a bag of weight {} is {}'.format(bagWeight, result)


