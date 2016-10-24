
# given an array find whether it has 3 values that can add up to a number k
# can repeat values

# approach is to do one pass through the values
# and from there do another check on the array if it has to values that sum up to k - A[i]

# runtime is O(nlogn) + O(n^2)

def hasTwoSum(values, k):

    # values must be sorted
    # start at a[0] + a[n-1]
    # if sum is < k, move leftmost
    # else, move rightmost

    start = 0
    end = len(values)-1

    while start < end:

        sumOfTwo = values[start] + values[end]
        if sumOfTwo == k:
            print 'the values are {} and {}'.format(values[start], values[end])
            return True
        elif sumOfTwo < k:
            start += 1
        else:
            end -= 1

    return False


def hasThreeSum(values, k):

    values.sort()
    print 'after sorting', values, 'looking for a value of', k

    for v in values:
        if hasTwoSum(values, k-v):
            print 'exiting with', v, 'found', k-v
            return True

    return False


# 2, 3, 5, 7, 11
a = [11, 2, 5, 7, 3]
print 'original list', a

hasThreeSum(a, 21)



