
# array must be sorted
a = [2, 4, 10, 10, 10, 18, 20]

# pass the array and the element we wish to find
def binarySearch(arr, x):

    # define low, high indexes
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (high + low) / 2
        
        if x == arr[mid]:
            return mid
        elif x < arr[mid]:
            # if value is less than the middle
            # use lower half by settin ga new high
            high = mid - 1
        else:
            # value is greater than mid
            # use later half by setting a new low
            low = mid + 1

    return -1

print a
print binarySearch(a, 10)








