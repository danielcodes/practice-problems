
# sort an almost sorted array
# given that no element is more than k values away

# approach, use a min-heap of k+1 size, and pop
# add a value from the list and repeat, until the heap is left with k+1 elements
# empty the heap then

# O(nlogk) time
# O(k) space

from heapq import heappush, heappop

def sortAlmostSorted(numbers, k):

    h = []
    result = []
    i = 0

    # fill heap
    while i < k:
        heappush(h, numbers[i])
        i += 1

    # step through the list
    while i < len(numbers):
        heappush(h, numbers[i])
        result.append(heappop(h))
        i += 1

    # empty the rest
    while h:
        result.append(heappop(h))

    return result

l = [3, -1, 2, 6, 4, 5, 8]
print 'the original list is', l
print 'after sorting, the result is', sortAlmostSorted(l, 2)



