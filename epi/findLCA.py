
# finding the least common ancestor for two nodes that have parent pointers
# approach is to first find the depths of each node and bring them to the same height
# from there, go up until they land on the same parent

# O(h), worse case traversal is the height of tree
# O(1), no additional space

from BinaryTreeNode import Node, printInOrder

def getDepth(node):

    height = 0
    while node.parent:
        height += 1
        node = node.parent

    return height

def findLCA(first, second):

    h1, h2 = getDepth(first), getDepth(second)

    # say first is the deeper one
    if h1 < h2:
        first, second = second, first

    # move the deeper one, by the difference
    steps = abs(h1 - h2)
    while steps:
        first = first.parent
        steps -= 1

    # now go up in tandem 
    while first != second:
        first = first.parent
        second = second.parent

    return first


a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
e = Node(5)
f = Node(6)
g = Node(7)

a.left = b
a.right = c
b.left = d
b.right = e
c.left = f
e.left = g

# ugh, gotta set the parents
b.parent = a
c.parent = a
d.parent = b
e.parent = b
f.parent = c
g.parent = e

print 'the inorder traversal is', printInOrder(a)
print 'the LCA of 3 and 7 is', findLCA(c, g).value
print 'the LCA of 4 and 7 is', findLCA(d, g).value


