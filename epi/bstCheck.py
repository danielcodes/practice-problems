
# check whether a a binary tree is a binary search tree
# is it a bst if at each node, all nodes in the left are smaller
# and all nodes on the right are larger

#     10
#   5    20
# 3   8
#    7

# valid, but if 8 gets a right child of 15, then boom

class Node:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# the utility
def isBSTUtil(node, lowerB, upperB):

    # base cases
    if node == None:
        return True

    # do the check
    if node.value < lowerB or node.value > upperB:
        return False

    # recurse for both left and right
    return isBSTUtil(node.left, lowerB, node.value) and isBSTUtil(node.right, node.value, upperB)


# this function makes the call
def isBST(root):
    return isBSTUtil(root, -float('infinity'), float('infinity'))


a = Node(10)
b = Node(5)
c = Node(20)
d = Node(3)
e = Node(8)
f = Node(7)

# to make it fail later
g = Node(15)

a.left = b
a.right = c
b.left = d
b.right = e
e.left = f


print 'the tree'
print '#     10'
print '#   5    20'
print '# 3   8'
print '#    7 |15|'


print 'checking if binary tree is a BST', isBST(a)

# add the right child
e.right = g

print 'checking if binary tree is a BST with 15 added,', isBST(a)


