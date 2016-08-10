
# count occurrences of a number in a sorted list
# get first and last occur and return the difference of these indices

# a modified binary search
# last param is a flag, for first or last occur
def binarySearch(arr, x, first):

    low = 0
    high = len(arr) - 1
    result = -1

    while low <= high:
        mid = (high + low) / 2
        
        if x == arr[mid]:
            result = mid

            # first or last
            if first:
                high = mid - 1 
            else:
                low = mid + 1

        elif x < arr[mid]:
            high = mid - 1
        else:
            low = mid + 1

    return result


if __name__ == '__main__':

    a = [2, 4, 10, 10, 10, 18, 20]

    print a

    value = input('enter a value to find ')

    first = binarySearch(a, value, 1)
    if first == -1:
        print 'Count of {} is {}'.format(value, 0)
    else:
        last = binarySearch(a, value, 0)
        print 'Count of {} is {}'.format(value, last-first+1)


