
# implement an inorder traversal nonrecursively
# approach, two two variables, prev and current to move throughout
# the tree. 3 possibilities as we move, prev is the parent
# prev is the left child, and both sides have been explored
# have access to parent node

from BinaryTreeNode import Node, printInOrder

def nonrecursiveInorder(root):

    result = []

    prev = None
    curr = root

    while curr != None:

        next_ = None
        # 3 nested ifs... sheesh
        # descending to either left or right
        if curr.parent == prev:

            # ugh, too many darn conditionals here
            if curr.left != None:
                next_ = curr.left
            else:
                result.append(curr.value)
                if curr.right:
                    next_ = curr.right
                else:
                    next_ = curr.parent
        elif curr.left == prev:
            # after finishing the left
            result.append(curr.value)
            if curr.right:
                next_ = curr.right
            else:
                next_ = curr.parent
        else:
            # finished with both left and right
            next_ = curr.parent

        # update prev and current
        prev = curr
        curr = next_

    return result

#     10
#   5    15 
# 3   8
#    7

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

# set up parents, ugh
a.parent = None
b.parent = a
c.parent = a
d.parent = b
e.parent = b
f.parent = e

print '#     10'
print '#   5    15' 
print '# 3   8'
print '#    7'


# 3 5 7 8 10 15
print 'the inorder traversal is', printInOrder(a)
result = nonrecursiveInorder(a)
print 'the values in the nodes from nonrecursiveInorder is', result


