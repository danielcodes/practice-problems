
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

# start a base case by setting the last node to head and return to start at second last
# set up 'ahead' node, make it point to current
# and make currynt point to nada

'''
   if (list == null) return null; // first question

    if (list.next == null) return list; // second question

    // third question - in Lisp this is easy, but we don't have cons
    // so we grab the second element (which will be the last after we reverse it)

    ListNode secondElem = list.next;

    // bug fix - need to unlink list from the rest or you will get a cycle
    list.next = null;

    // then we reverse everything from the second element on
    ListNode reverseRest = Reverse(secondElem);

    // then we join the two lists
    secondElem.Next = list;

    return reverseRest;
'''

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




