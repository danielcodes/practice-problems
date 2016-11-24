
# given a set of heights, find the largest rectangle contained in the heights
# brute force is to look at each height A[i], and look left and right till there is a taller height
# and then compute the found rectangle, this takes O(n^2)
# better approach, move through the values pushing them onto a stack, if the current value
# is smaller than the value on top of the stack, compute heights until idx > top (height-wise)

def computeLargestRectangle(heights):

    pillarIndices = []
    maxArea = 0
    for i in range(len(heights)+1):

        # multiple checks to short circuit
        # if the current is equal to top, set top to be equal to current
        if (len(pillarIndices) != 0) and (i < len(heights)) and (heights[i] == heights[pillarIndices[-1]]):
            pillarIndices.pop()
            pillarIndices.append(i)

        # compute areas when curr < top, or if it's the end
        while (len(pillarIndices) != 0) and isPillarOrEnd(heights, i, pillarIndices[-1]):

            # 5 print statements to debug
            # print 'current index', i, 'current top of stack', pillarIndices[-1]
            # when it reaches the end, it's not messing with the indices
            # just the indices on the stack
            # take the height, and pop it out
            height = heights[pillarIndices[-1]]
            pillarIndices.pop()

            # width is computed the the top-1 item
            width = 0
            if not pillarIndices:
                width = i
            else:
                width = i - pillarIndices[-1] -1

            # print 'h and w are', height, width
            # print 'max old and new', maxArea, height*width
            maxArea = max(maxArea, height * width)
            # print 'max after', maxArea, '\n'

        pillarIndices.append(i)
        # print pillarIndices

    return maxArea


def isPillarOrEnd(heights, curr, last):

    if curr < len(heights):
        # True if curr height is smaller
        # keep computing areas
        return heights[curr] < heights[last]
    else:
        # reached the end
        return True


heights = [1, 2, 2, 3, 1]
result = computeLargestRectangle(heights)
print 'the maximum area found in {} is {}'.format(heights, result)

heights = [1, 4, 2, 5, 6, 3, 2, 6, 6, 5, 2, 1, 3]
result = computeLargestRectangle(heights)
print 'the maximum area found in {} is {}'.format(heights, result)


