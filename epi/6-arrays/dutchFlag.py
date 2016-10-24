
# dutch flag problem
# given an array and a pivot x
# rearrange so that values on left are < x, middle = x, and right > x

# do it in one pass, 4 partitions

a = [3, 6, 1, 0, 3]

def dutchFlag(a, pivot):
	
    start = 0
    equal = 0
    end = len(a)
    
    while equal < end:
            
        # 3 cases, <, > and == pivot
        # quite tricky
        if a[equal] < pivot:
            # moves elements to the front and moves ptr forward
            a[start], a[equal] = a[equal], a[start]
            start += 1
            equal += 1
        elif a[equal] == pivot:
            # keep moving along
            equal += 1
        else:
            # swap with last element, but don't move as new value needs to be examine
            end -= 1
            a[end], a[equal] = a[equal], a[end]
            
		
print 'input is {} and pivot is {}'.format(a, 3)
dutchFlag(a, 3)
print 'result is', a
	


