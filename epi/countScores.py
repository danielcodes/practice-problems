
# counting the ways to get a sum given an array of numbers
# ie s = 5, a = [1, 2, 3], given the denominations find how many ways
# are there to make 5

# TODO, generate the arrays that cointain the numbers that sum up to s

def waysToGetNum(s, numbers):
	
    result = [0]*(s+1)
    result[0] = 1
    
    for num in numbers:
        for i in range(num, s+1):
            result[i] += result[i-num]
                        
        print 'using', num, 'and prev coins', result
	
a = [1, 2, 3]
s = 5

# ways to get 5 counting, 11111, 2111, 221, 311, 32

waysToGetNum(s, a)
	
