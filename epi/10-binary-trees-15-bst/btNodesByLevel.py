
# given a binary tree, return a list of lists
# each list containing the nodes at that height
# ie
#    5
#  4    3
# 1 6  9 8
# output should be, [[5], [4, 3], [1, 6, 9, 8]]

# approach is use a queue to hold the nodes at each level
# and a size variable indicating the number of nodes at that level
# as we move through the queue, exhaust the size variable and push the items into another list
# when size reaches 0, and the list containing the node values is not empty, push it to result

# O(n) time, n being the number of nodes
# O(m) space, m being the max number of nodes in a level

from BinaryTreeNode import Node, printInOrder
from collections import deque

def treeNodesPerLevel(root):

    nodesToProcess = deque()
    nodesToProcess.append(root)
    countNodes = len(nodesToProcess)

    result = []
    oneLevelNodes = []

    # start iteration
    while nodesToProcess:

        # doesn't handle edge cases too well
        current = nodesToProcess.popleft()
        oneLevelNodes.append(current.value)
        countNodes -= 1

        if current.left:
            nodesToProcess.append(current.left)

        if current.right:
            nodesToProcess.append(current.right)

        # no more nodes to process at this level
        if countNodes == 0:
            countNodes = len(nodesToProcess)

            # make sure that there are nodes to add
            result.append(oneLevelNodes)
            oneLevelNodes = []

    return result


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

c.right = g
print 'with a full tree'
print 'the inorder traversal is', printInOrder(a)
print 'nodes per level are', treeNodesPerLevel(a)
print '\n'

c.right = None
e.left = g
print 'moving the 7 the left child of 5'
print 'the inorder traversal is', printInOrder(a)
print 'nodes per level are', treeNodesPerLevel(a)


