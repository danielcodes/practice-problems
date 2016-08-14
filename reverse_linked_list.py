
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

# does not return the head, assumes it is a global
# http://stackoverflow.com/questions/354875/reversing-a-linked-list-in-java-recursively

# amazing recursive solution, must read little lisper
def reverseRec(head):

    if head == None:
        return None

    if head.next == None:
        return head

    second = head.next

    head.next = None

    rest = reverseRec(second)
    second.next = head

    return rest

  
a = Node(30, None)
a = insert(a, 40)
a = insert(a, 50)
a = insert(a, 60)

print 'normal'
printList(a)

a = reverseRec(a)

print 'reversed'
printList(a)




