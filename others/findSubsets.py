
def findSubsets(a):
    
    # base case
    if len(a) == 1:
        return [a]
    
    last = a[-1]
    arrNoLast = a[:-1]
    
    subsetsNoLast = findSubsets(arrNoLast)
    
    totalSubsets = []
    
    # copy values returned from subsetsNoLast
    # also adding the last value to each subset, creating a new one
    for val in subsetsNoLast:
        totalSubsets.append(val)
        totalSubsets.append(val + [last])
        
    totalSubsets.append([last])
    
    return totalSubsets

a = [1, 2, 3]
print 'the subsets of', a, 'are', findSubsets(a)
