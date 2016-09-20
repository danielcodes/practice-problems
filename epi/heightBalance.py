
# implementing the height balance check for binary trees
# height balance is when the height on the left and the height on the right do not differ by more than 1

class BinaryTreeNode:
    
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        
        
def isHeightBalanced(root):
    
    # base case 
    if root == None:
        # (height balanced, height)
        return (True, -1)
        
    # recurse on left and right
    left_result = isHeightBalanced(root.left)
    if left_result[0] != True:
        return (False, 0)
        
    right_result = isHeightBalanced(root.right)
    if right_result[0] != True:
        return (False, 0)
    
    # check for height balance here
    # return Node with new height
    is_balanced = abs(left_result[1] - right_result[1]) <= 1
    height = max(left_result[1], right_result[1]) + 1 
    
    return (is_balanced, height)
        
        
# createa tree
a = BinaryTreeNode(1)
b = BinaryTreeNode(2)
c = BinaryTreeNode(3)
d = BinaryTreeNode(4)
e = BinaryTreeNode(5)
f = BinaryTreeNode(6)
g = BinaryTreeNode(7)

a.left = b 
a.right = c 
b.left = d 
b.right = e
e.right = f
f.left = g

def printInorder(root):
    
    if root != None:
        printInorder(root.left)
        print root.value
        printInorder(root.right)
        
# printInorder(a)

print isHeightBalanced(a)


