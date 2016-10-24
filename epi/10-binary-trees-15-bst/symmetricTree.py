
# check for a symmetric tree
# a tree is symmetric if by drawing a line down the root
# the nodes are the same, keys included

# approach, to recurse down, it must pass 3 checks
# that the nodes are the same, and go down far left and right
# and inner left and right

from BinaryTreeNode import Node, printInOrder

def isTreeSymmetric(root):

    return root == None or symmetricTreeHelper(root.left, root.right)


# recursive step
def symmetricTreeHelper(leftTree, rightTree):

    # handle 3 cases
    # base case, left and right are None
    if leftTree == None and rightTree == None:
        return True
    elif leftTree != None and rightTree != None:
        # both subtrees are not None
        # 3 checks, the nodes and recurse down
        # print 'currently comparing', leftTree.value, rightTree.value
        return (leftTree.value == rightTree.value) and symmetricTreeHelper(leftTree.left, rightTree.right) and symmetricTreeHelper(leftTree.right, rightTree.left)
    
    # one node exists, the other doesn't
    return False
       

# inorder is 6, 2, 3, 314, 3, 2, 6
a = Node(314)
b = Node(6)
c = Node(6)
d = Node(2)
e = Node(2)
f = Node(3)
g = Node(3)

a.left = b
a.right = c
b.right = d
c.left = e
d.right = f
e.left = g

print printInOrder(a)
print 'is this tree symmetric?', isTreeSymmetric(a)


