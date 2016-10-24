
# given an integer in array form, add one to it
# [1, 2, 9] -> [1, 3, 0]
# if there is a leftover carry, shift values to the right
# [9, 9] -> [1, 0], lose a LSB

# O(n) time, worse case, when the carry moves all the way to the left
# O(1) space

from collections import deque

def incrementPrecisionInt(number):
    
    # add one to last digit
    result = deque(number)
    result[-1] += 1
    lastIndex = len(result)-1 

    # do not operate on the first digit
    while result[lastIndex] == 10 and lastIndex > 0:

        # set the last digit to 0
        result[lastIndex] = 0

        # decrese index and add the carry in
        lastIndex -= 1
        result[lastIndex] += 1
        
    # to imitate the shift, I'm going to add to the left and pop from right
    if result[0] == 10:
        result[0] = 0
        result.appendleft(1)
        result.pop()

    return result


a = [1, 2, 9]
print 'the precision int is,', a
print 'the result is,', incrementPrecisionInt(a)

a = [9, 9, 9]
print '\nthe precision int is,', a
print 'the result is,', incrementPrecisionInt(a)


