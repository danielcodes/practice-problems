
# check whether two lists have an element in common
# approach is to find the lengths, move the longer list by their difference
# move at the same time until they arrive at an equal node or end

# O(n) time, two O(n) traversals of each list
# O(1) space

from LinkedListNode import Node, printList, findLength, advanceByK

def isThereOverlap(list1, list2):

    l1 = findLength(list1)
    l2 = findLength(list2)
    diff = abs(l1-l2)

    if l1 > l2:
        list1 = advanceByK(list1, diff)
    else:
        list2 = advanceByK(list2, diff)

    while list1 and list2:

        if list1 == list2:
            return list1
        list1 = list1.next
        list2 = list2.next

    # none
    return list1


# 13 2 4 7 9
d = Node(9)
e = Node(7, d)
f = Node(4, e)
g = Node(2, f)
h = Node(13, g)

# 3 4 7 9
i = Node(3, f)

print 'the two lists are' 
printList(h)
printList(i)

print 'the overlapping node is', isThereOverlap(h, i).value


