
# finding the majority element
# find the element that appears the most in an array
# guaranteed that this value covers more than half of the array

# approach, start with the first value, and iterate
# if next value is equal increment, otherwise decrement
# if count is 0, set the next char as the item to count

# the explanation behind this is that if we have two groups, one with the majority element
# one without, and we remove a value from each, there are two posibilities
# -1, -2 or -0, -2, this will eventually exhaust
# the numbers and we'll be leftover with the majority element

def findMajorityElement(values):

    current = None
    count = 0
    i = 0

    while i < len(values):

        if count == 0:
            current = values[i]
            count = 1
        elif values[i] == current:
            count += 1
        else:
            count -= 1

        i += 1

    return current


values = ['b', 'a', 'c', 'a', 'a', 'b', 'a', 'a', 'c', 'a']
print 'the stream of values is', values
print 'the majority element is', findMajorityElement(values)


