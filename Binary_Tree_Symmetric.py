class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isMirror(t1, t2):
    if not t1 and not t2:
        return True
    if not t1 or not t2:
        return False
    return (t1.val == t2.val and 
            isMirror(t1.left, t2.right) and 
            isMirror(t1.right, t2.left))

def isSymmetric(root):
    if not root:
        return True
    return isMirror(root.left, root.right)



root1 = TreeNode(1)
root1.left = TreeNode(2)
root1.right = TreeNode(2)
root1.left.left = TreeNode(3)
root1.left.right = TreeNode(4)
root1.right.left = TreeNode(4)
root1.right.right = TreeNode(3)

print("Example 1:", isSymmetric(root1))  

root2 = TreeNode(1)
root2.left = TreeNode(2)
root2.right = TreeNode(2)
root2.left.right = TreeNode(3)
root2.right.right = TreeNode(3)

print("Example 2:", isSymmetric(root2))
