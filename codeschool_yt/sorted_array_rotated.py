
# looking for a pivot
# it is lower than its previous and next element

# works only with no duplicates

def findRotationCount(arr):
    
    length = len(arr)
    low = 0
    high = length - 1

    while low <= high:
        
        # 4 cases
        # already sorted, we're at the pivot
        # look opposite side depending on which side is already sorted
        if arr[low] <= arr[high]:
            return low

        mid = (low + high) / 2
        next_ = (mid+1) % length
        prev = (mid-1+length) % length

        if arr[mid] <= a[next_] and arr[mid] <= arr[prev]:
            return mid
        elif arr[mid] <= arr[high]:
            high = mid-1
        elif arr[mid] >= arr[low]:
            low = mid+1
        else:
            pass

    return -1


a = [15, 22, 23, 28, 31, 38, 5, 6, 8, 10, 12]

print a
print 'the numuber of rotations in a is ', findRotationCount(a)



