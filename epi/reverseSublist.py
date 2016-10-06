
# reversing a sublist in a linked list

from LinkedListNode import Node, printList

def reverseSublist(l, start, end):
    
    # needs work, handling edge cases
    # what if start is the head of the list?
    
    # assume the list count start at 1
    head = l 
    dummy_head = l
    
    # move predecessor to the node before start 
    for i in range(1, start-1):
        dummy_head = dummy_head.next
    
    # printList(dummy_head)
    
    node_iter = dummy_head.next
    while start < end:
        
        print 'at iteration number', start
        
        temp = node_iter.next
        node_iter.next = temp.next
        temp.next = dummy_head.next
        dummy_head.next = temp
        
        printList(head)
        
        start += 1
        
    return head


# 1 -> 2 -> 3
a = Node(2)
b = Node(7, a)
c = Node(5, b)
d = Node(3, c)
e = Node(11, d)

print 'original list'
printList(e)

reverseSublist(e, 2, 4)


