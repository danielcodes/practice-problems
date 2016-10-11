
# given a BST, return the k largest elements in decreasing order
# ie. an inorder traversal of [3, 5, 7, 8, 10, 15] and k = 3
# returns [15, 10, 8]

# approach is to use a reverse inorder traversal and grab k elements
# once k elements have been grabbed, no need to recurse further

from BinaryTreeNode import Node, printInOrder

def getElements(k, values, root):

    # a reverse inorder traversal, right, root and left
    # this gives the a list of nodes in decreasing order
    if root:
        getElements(k, values, root.right)

        # this check occurs at each node
        if len(values) < k:
            values.append(root.value)
            getElements(k, values, root.left)


def getKElements(root, k):

    values = []
    getElements(k, values, root)
    return values


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
print 'the 3 largest elements are,', getKElements(a, 3)

