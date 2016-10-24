
# given an array of values which represent vertical lines
# find the maximum area that can be trapped between a range of lines

# approach, close down from both ends
# get rid of the lesser value, if they're the same move both
# all the while, updating the max if required

def findMaxWaterTrapped(lines):

    i = 0
    j = len(lines)-1
    maxWaterTrapped = 0

    while i < j:

        waterTrapped = (j-i) * min(lines[i], lines[j])
        maxWaterTrapped = max(maxWaterTrapped, waterTrapped)

        if lines[i] < lines[j]:
            i += 1
        elif lines[i] > lines[j]:
            j -= 1
        else:
            i += 1
            j -= 1

    return maxWaterTrapped 


lines = [1, 2, 1, 3, 4, 4, 5, 6, 2, 1, 3, 1, 3, 2, 1, 2, 4, 1]
print 'the vertical lines are'
print lines
print 'the maximum amount of water that can be trapped is', findMaxWaterTrapped(lines)


