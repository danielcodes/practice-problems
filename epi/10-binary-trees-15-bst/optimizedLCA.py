
# this is problem 13.4, the hashtable sect but the main DT is trees
# find the LCA optimally so that the time complexity equals to the distance
# approach, move up the two nodes at the same time while hashing the parent
# as soon as the prev parent is seen, we have a result

# O(d) time, d is the distance between the nodes and the LCA
# O(n) space, for storing the nodes seen so far

from BinaryTreeNode import Node, printInOrder

def optimizedLCA(node1, node2):

    # keep (value, True)
    visited = {}

    while node1 or node2:

        if node1:
            # if the node has been seen, that's the LCA
            # otherwise, store and move up
            if node1 in visited:
                return node1
            visited[node1] = True

            node1 = node1.parent

        if node2:
            if node2 in visited:
                return node2
            visited[node2] = True

            node2 = node2.parent

    # the nodes are not in the same tree
    raise Exception('the nodes are not in the same tree')


a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
e = Node(5)
f = Node(6)

a.left = b
a.right = c
b.left = d
b.right = e
e.left = f

# set up parents, ugh
a.parent = None
b.parent = a
c.parent = a
d.parent = b
e.parent = b
f.parent = e

print '#     1'
print '#   2   3' 
print '# 4   5'
print '#    6'

print 'the inorder traversal is', printInOrder(a)

n1 = d
n2 = f
result = optimizedLCA(n1, n2)
print 'the optimized LCA for {} and {} is {}'.format(n1.value, n2.value, result.value)

n1 = d
n2 = c
result = optimizedLCA(n1, n2)
print 'the optimized LCA for {} and {} is {}'.format(n1.value, n2.value, result.value)


