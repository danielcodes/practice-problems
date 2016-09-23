
# merging two sorted arrays
# [5, 13, 17, _, _, _, _, _]
# [3, 7, 11, 19]
# [3, 5, 7, 11, 13, 17, 19, _]

# trick here is to populate starting at the end
# and exhaust starting from the end of the two arrays

def mergeLists(a, m, b, n):
    '''a and b are list, and m and n the # of elments
    a has extra space, enough to merge the values of b
    '''
    
    # tail pointers
    a_tail = m-1
    b_tail = n-1
    result_index = m+n-1
    
    # exhaust arrays until one finishes
    while a_tail >= 0 and b_tail >= 0:
        
        if a[a_tail] > b[b_tail]:
            a[result_index] = a[a_tail]
            result_index -= 1 
            a_tail -= 1
        else:
            a[result_index] = b[b_tail]
            result_index -= 1
            b_tail -= 1 
    
    # at this point one of the lists is exhausted
    # only need to consider if b hasn't been exhausted
    # if all values of b are gone, they must of been higher so a is sorted
    
    while b_tail >= 0:
        a[result_index] = b[b_tail]
        result_index -= 1
        b_tail -= 1

    return a            
        

a = [5, 13, 17, 0, 0, 0, 0]
b = [3, 7, 11, 19]

print a, 'to be merged with', b 
print 'after merging', mergeLists(a, 3, b, 4)
    
    

