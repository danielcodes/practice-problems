
# find the LCA in a BST, no access to parent node
# approach, move down until you land at key than is within
# the range [l, u], lower and upper bound

from BinaryTreeNode import Node, printInOrder

def findLCAinBST(root, lower, upper):

    # move the root until it is in the range [l, u]
    # if root is either l or u, it will not go in
    # trap in the range, equal counts
    while not (root.value >= lower.value and root.value <= upper.value):

        # lca in the right
        if root.value < upper.value:
            root = root.right
        else:
            # otherwise left
            root = root.left

    return root.value
    

a = Node(10)
b = Node(5)
c = Node(20)
d = Node(3)
e = Node(8)
f = Node(7)
g = Node(9)

a.left = b
a.right = c
b.left = d
b.right = e
e.left = f
e.right = g

print 'the tree'
print '#     10'
print '#   5    20'
print '# 3   8'
print '#    7 9'

print 'the LCA for the nodes {} and {} is {}'.format(d.value, g.value, findLCAinBST(a, d, g))
print 'the LCA for the nodes {} and {} is {}'.format(f.value, g.value, findLCAinBST(a, f, g))
print 'the LCA for the nodes {} and {} is {}'.format(a.value, c.value, findLCAinBST(a, a, c))
print 'the LCA for the nodes {} and {} is {}'.format(b.value, a.value, findLCAinBST(a, b, a))


