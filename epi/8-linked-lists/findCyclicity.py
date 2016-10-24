
# find whether a linked list contains a cycle
# if yes, return the first node in cycle, else, -1

# approach is to use the two iterator approach to get inside the cycle
# then find the length and use two pointers one at start and one at length L
# iterate until the pointers meet

from LinkedListNode import Node, printList

def checkCyclicity(root):

    slow = root
    fast = root

    # note the check here, takes care of edge cases
    # if fast.next exists, it can move to fast.next.next
    while fast and fast.next:

        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            
            # find the length
            fast = fast.next
            length = 1
            
            while fast != slow:
                fast = fast.next
                length += 1

            # create the stick of length L
            end = root
            while length > 0:
                end = end.next
                length -= 1

            start = root
            while start != end:
                start = start.next
                end = end.next

            print 'the first node in the cycle is', start.value
            return start.value

    # loop has finished traversing the list
    print 'no cycle in this list\n'
    return False


# 11 - 3 - 5 - 7 - 2
#          |-------|

a = Node(2)
b = Node(7, a)
c = Node(5, b)
d = Node(3, c)
e = Node(11, d)

# create cycle

print 'original list'
printList(e)

checkCyclicity(e)

print 'now linking 2 to 5'
printList(e)
print '           |---------|'

a.next = c

checkCyclicity(e)


