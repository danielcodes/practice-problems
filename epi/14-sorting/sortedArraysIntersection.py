

# intersection of two sorted arrays
# same principle as merging two lists, but only take the values if they're equal

def getIntersection(a, b):
    
    i = 0
    j = 0
    intersection = []
    
    while i<len(a) and j<len(b):
        
        # needs additional check for duplicates
        # if it's the first element is ok
        # or if the value is not equals to the one before it 
        if a[i] == b[j] and (i == 0 or a[i] != a[i-1]):
            intersection.append(a[i])
            i += 1 
            j += 1
        elif a[i] < b[j]:
            i += 1 
        else:
            j += 1 
            
    print intersection



# result is, [3, 5]
a = [1, 3, 3, 5, 7, 11]
b = [3, 3, 7, 15, 31]

getIntersection(a, b)


