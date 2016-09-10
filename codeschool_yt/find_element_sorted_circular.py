
# another modification of binary search
# does not work with duplicates

def circularListSearch(arr, x):
    
    length = len(arr)
    low = 0
    high = length - 1

    while low <= high:
        
        # 4 cases
        mid = (low + high) / 2
        if x == arr[mid]: 
            return mid

        # careful not to touch that mid element
        # find which part is sorted
        if arr[mid] <= a[high]: 

            # search right 
            if x > arr[mid] and x <= arr[high]: 
                low = mid+1
            else:
                high = mid-1
        else:
            # left half is sorted
            if x >= arr[low] and x < arr[mid]:
                high = mid-1
            else:
                low = mid+1

    return -1


a = [12, 14, 18, 21, 3, 6, 8, 9]

print a
print 'the index is ', circularListSearch(a, 21)
print 'the index is ', circularListSearch(a, 1)





