# think I'll be importing from here a lot

class Node(object):
 
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = next_node

# inserts to the tail
def insert(head, data):

    if head == None:
        head = Node(data, None)
        return head
    
    head_ref = head
    
    # first gotta get to the last element that has next as None
    while head.next != None:
        # keep moving
        head = head.next
    
    # at the last node
    newNode = Node(data, None)
    head.next = newNode
    
    return head_ref

def printList(head):
    while head != None:
        print head.data
        head = head.next


def printForwardRec(head):
    if head == None:
        return

    print head.data
    printForwardRec(head.next)


def printReverseRec(head):
    if head == None:
        return

    printReverseRec(head.next)
    print head.data





