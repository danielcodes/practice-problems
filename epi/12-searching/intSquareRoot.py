
# given a number k, find the largest square that is less than k
# ie. if k = 40, the answer is 6, 36 < 40

# approach is to use a binary search variant to create a range where
# the left is less than or equal to k and the right is higher
# this results in the answer being left-1

def getIntSquare(k):

    start = 0
    end = k

    while start <= end:

        mid = start + (end-start)/2
        # print 'the current range is', start, end, 'and the middle is', mid
        
        # go right if <= k
        if mid*mid <= k:
            start = mid+1
        else:
            end = mid-1

    return start-1


a = getIntSquare(25)
print 'the largest square less than or equal to 25 is', a, '\n'

b = getIntSquare(20)
print 'the largest square less than or equal to 20 is', b


