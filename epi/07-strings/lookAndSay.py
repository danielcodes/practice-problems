
# look and say problem
# a sequence that start with one and follows by counting digits followed by the digits <count, digit>
# ie. n=4, [1, 11, 21, 1211, 111221, ...]
# return the value as a string

def lookAndSay(n):
	
    values = [0 for i in range(n+1)]
    values[0] = '1'
    
    print 'initial values are'
    print values
    
    # gotta build up each value
    for j in range(1, n+1):
            
        result = ''
        prevVal = values[j-1]
        # two variables needed
        current = prevVal[0]
        count = 1

        # stepping through the string
        for k in range(1, len(prevVal)):
                
            # char is same, add count
            if prevVal[k] == current:
                count += 1
            else:
                # otherwise, add it to result
                # and reset
                result += (str(count) + current)
                current = prevVal[k]
                count = 1
                
        # gotta add it at the end too, sheesh
        result += (str(count) + current)
                        
        values[j] = result
        print values
    
    return values[n]

n = 7
result = lookAndSay(n)
print 'the {}th value for the look-and-say sequence is {}'.format(n, result)


