
from Linkedlist import Node, insert, printList

# reversing a linked list
# 2 approaches, iterative and recursion

def reverse(head):

    prev = None
    current = head
    
    while current is not None:
        next = current.next
        current.next = prev
        prev = current
        current = next
    
    head = prev
    
    return head 

a = Node(30, None)
a = insert(a, 40)
a = insert(a, 50)
a = insert(a, 60)

print 'normal'
printList(a)

a = reverse(a)

print 'reversed'
printList(a)



