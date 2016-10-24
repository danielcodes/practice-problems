
# remove k last element in a linked list
# easily found if length is known, but it is not provided

# approach is to build a k+1 stick (2 iterators) and get to the end
# this leaves the first at the k+1 value (predecessor of the node that we want to remove)
# removing k is easy from here

# ie
# 1 -> 2 -> 3 -> 4 -> 5, k = 2
# *---------*
# move it   *---------*
# change linkage of 3 to 5

from LinkedListNode import Node, printList, createDummyList

def removeKLast(head, k):

    # assumes that list has at least k nodes
    result = head
    first = head
    second = head

    # advance k steps
    while k:
        second = second.next
        k -= 1

    # move to the end
    while second.next != None:
        first = first.next
        second = second.next

    # create new linkage
    first.next = first.next.next

    return result


print 'original list'
head = createDummyList()
k = 3
printList(head)

print 'after removing the {}th element'.format(k)
result = removeKLast(head, k)
printList(result)



