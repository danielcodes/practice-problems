
# given a BST and a value
# find the first key greater than value as seen in an inorder traversal

# approach is to traverse down the tree and save the answer so far
# returns -1 for nonfound values

from BinaryTreeNode import Node, printInOrder

def findGreaterKey(root, value):

    result = -1
    while root:

        # print 'currently visiting', root.value
        if root.value > value:
            result = root.value
            root = root.left
        else:
            root = root.right

    return result


a = Node(10)
b = Node(5)
c = Node(15)
d = Node(3)
e = Node(8)
f = Node(7)

a.left = b
a.right = c
b.left = d
b.right = e
e.left = f

print 'the inorder traversal is', printInOrder(a)
print 'the first key greater than 6 is', findGreaterKey(a, 6)
print 'the first key greater than 8 is', findGreaterKey(a, 8)
print 'the first key greater than 11 is', findGreaterKey(a, 11)
print 'the first key greater than 20 is', findGreaterKey(a, 20)
 

