
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
 
