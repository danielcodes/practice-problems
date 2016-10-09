
# module for binary trees

class Node:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None


def printInOrder(root):

    nodes = []
    printInOrderUtil(root, nodes)
    return nodes

def printInOrderUtil(root, nodes):

    if root:
        printInOrderUtil(root.left, nodes)
        nodes.append(root.value)
        printInOrderUtil(root.right, nodes)


