
# given a number, reverse the digits
# ie. 456 -> 654, -1235 -> -5321

# approach is to use modulo to slowly get the last digit

def reverseDigits(number):

    neg = False
    result = 0
    remainingNum = number

    # using module on a negative number gets real ugly
    if number < 0:
        neg = True
        remainingNum = -number # turn it positive

    while remainingNum:

        # result moves one decimal place each time
        # thus the x10
        result = result * 10 + remainingNum % 10
        remainingNum /= 10

    # account for negative
    if neg:
        result = -result
    return result 


n = -1234
print 'the starting number is,', n
print 'after reversing,',reverseDigits(n)

n = 4927
print 'the starting number is,', n
print 'after reversing,',reverseDigits(n)



