
# build a minimum height BST from a sorted array
# approach, we get the min bst by picking the middle value
# as the root, do this recursively to build the whole tree

from BinaryTreeNode import Node, printInOrder

def buildBSTHelper(values, start, end):

    if start >= end:
        return None

    mid = start + (end-start)/2
    # print start, end, mid
    return Node(values[mid], buildBSTHelper(values, start, mid), buildBSTHelper(values, mid+1, end))

def buildMinHeightBST(values):

    # base case
    # have to call with length and not length+1
    # since when there are two values remaining, [1,2]
    # the mid is always the left, and this issues one more
    # recursive call with two base cases, [1,1] and [2, 2]
    return buildBSTHelper(values, 0, len(values))


values = [0, 2, 5, 7, 9, 10]
print 'the original list is', values
result = buildMinHeightBST(values)
print 'after building the tree, the inorder traversal is', printInOrder(result)


