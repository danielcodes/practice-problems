
# given a linked list, say the head node is at index 0
# return a list such as the even nodes are in the front
# and odd nodes are behind it (even and odd mean indexes)

# approach keep a head node for each list even and odd
# step through the list and append accordingly

from LinkedListNode import Node, printList, createDummyList

def mergeEvenOdd(head):

    # assume that list has at least 3 elements
    evenH = head
    oddH = head.next 
    toggle = False
    evenIter = evenH
    oddIter = oddH

    # move to third node
    head = head.next.next
    while head:

        # as the node are being concatenated
        # gotta shift the iterator forward too
        if toggle:
            oddIter.next = head
            oddIter = oddIter.next
        else:
            evenIter.next = head
            evenIter = evenIter.next

        head = head.next
        toggle = not toggle

    # head's tail is odd's head
    evenIter.next = oddH
    oddIter.next = None

    return evenH

h = createDummyList()
print 'the original list is' 
printList(h)
result = mergeEvenOdd(h)
print 'after doing the even odd merge, the list becomes'
printList(result)


