
# faster way to sort a linked list
# approach, use a merge sort variation, splitting the list
# in two each time and merging them after

from LinkedListNode import Node, printList, createDummyList
from mergeSortedLists import mergeLists

def sortList(head):

    # base cases
    if head == None or head.next == None:
        return head

    pre_slow = None
    slow = head
    fast = head

    # at least two nodes
    while fast and fast.next:
        pre_slow = slow
        slow = slow.next
        fast = fast.next.next

    # split the list
    pre_slow.next = None

    return mergeLists(sortList(head), sortList(slow))
        
l = createDummyList()
print 'original list'
printList(l)

result = sortList(l)
print 'after sorting'
printList(result)

