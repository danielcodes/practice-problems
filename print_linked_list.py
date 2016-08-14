
# printing a linked list using recursion
# more efficient to iterate

from Linkedlist import Node, insert, printList, printForwardRec, printReverseRec

head = Node(1, None)
head = insert(head, 3)
head = insert(head, 5)
head = insert(head, 7)

# printList(head)

print 'printing with recursion baby'
printForwardRec(head)

print 'printing in reverse with recursion baby'
printReverseRec(head)



