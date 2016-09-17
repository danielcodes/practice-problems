
# merging two sorted linked lists


class Node:
    
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next
        

def printList(head):
    
    l = []
    while head != None:
        l.append(head.value)
        head = head.next
        
    l = ' -> '.join(map(str, l))
    print l
        

def mergeLists(l1, l2):
    
    # node to which we attach the values
    head = Node()
    tail = head
    
    # exhaust one of the lists first
    while l1 and l2:
        
        if l1.value <= l2.value:
            # append function was not working so..
            tail.next = l1
            tail = l1
            l1 = l1.next
        else:
            tail.next = l2
            tail = l2
            l2 = l2.next
            
    # append the rest of the list
    if l1:
        tail.next = l1
    else:
        tail.next = l2
        
    printList(head.next)
    return head.next


# 1 3 5
a = Node(5)
b = Node(3, a)
c = Node(1, b)

# 2 4 7 9
d = Node(9)
e = Node(7, d)
f = Node(4, e)
g = Node(2, f)

print 'before merging'
printList(c)
printList(g)

print 'after merging'
mergeLists(c, g)


