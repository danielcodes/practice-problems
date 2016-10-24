
# in a cyclically sorted list, find index of min value
# approach is to realize the invariant
# that for any m, if a[m] > a[n-1], min must be on the right
# if a[m] < a[n-1], min must be on the left
# this eventually converges to one value, the answer

def findMin(numbers):

    # when going left, the current mid
    # is a possible answer, so it doesn't change
    # on right, it's m-1
    start = 0
    end = len(numbers)-1

    while start < end:

        m = start + (end-start)/2
        # print start, end, m
        if numbers[m] > numbers[end]:
            start = m+1
        else:
            end = m

    return start


n = [21, 1, 2, 3, 5, 7, 9]
print 'the min index for {} is {}'.format(n, findMin(n))
m = [3, 5, 7, 9, 21, 1, 2]
print 'the min index for {} is {}'.format(m, findMin(m))


