
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


# reversing using stack
# this is overly complicated, I hate it
def reverseStack(head):

    s = []

    # first push all addresses into the stack
    # this brings
    temp = head
    while temp != None:
        s.append(temp)
        temp = temp.next

    # abusing variables
    temp = s[-1]
    head = temp
    s.pop()

    while s:
        temp.next = s[-1]
        s.pop()
        temp = temp.next

    temp.next = None

    return head


# ###############################################################

a = Node(30, None)
a = insert(a, 40)
a = insert(a, 50)
a = insert(a, 60)

print 'normal'
printList(a)

a = reverseStack(a)

print 'reversed'
printList(a)




