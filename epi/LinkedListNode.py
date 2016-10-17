
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
 

def findLength(head):

    l = 0
    while head != None:
        l += 1
        head = head.next
    return l


def advanceByK(head, k):

    while k:
        head = head.next
        k -= 1
    return head


