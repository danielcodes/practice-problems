
# given an array of chars and a string
# find the smallest substr that contains all chars

# ie [s i r  h e l l o]
# gives back [h e l l o  s i r]
# words are reversed

# reverses values in an array
def reverseChars(arr, start, end):

    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1
		
		
def reverseWords(arr):
	
    l = len(arr)
    # reverse first
    reverseChars(arr, 0, l-1)
    
    # using this start value is pretty neat
    # allows for resetting the looking for a new word step
    start = None
    for i in range(l):
        # 3 checks, found a word, last word and just move forward
        if arr[i] == '  ' and start != None:
            reverseChars(arr, start, i-1)
            start = None
        elif i == l-1 and start != None:
            reverseChars(arr, start, i)
        else:
            # not a space and not at last
            if start == None:
                start = i
        
		

a = [ 'p', 'e', 'r', 'f', 'e', 'c', 't', '  ', 'm', 'a', 'k', 'e', 's', '  ', 'p', 'r', 'a', 'c', 't', 'i', 'c', 'e' ]

print 'before', a		
reverseWords(a)		
print 'after', a


# this one's a doosy
a = [ 's', 'i', 'r', '  ', '  ', '  ', '  ', 'h', 'o', 'w' ]

print 'before', a		
reverseWords(a)		
print 'after', a


