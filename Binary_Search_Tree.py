class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isValidBST(root, low=float('-inf'), high=float('inf')):
    if not root:
        return True
    if not (low < root.val < high):
        return False
    return (isValidBST(root.left, low, root.val) and
            isValidBST(root.right, root.val, high))



root1 = TreeNode(2)
root1.left = TreeNode(1)
root1.right = TreeNode(3)

print(isValidBST(root1))  


root2 = TreeNode(5)
root2.left = TreeNode(1)
root2.right = TreeNode(4)
root2.right.left = TreeNode(3)
root2.right.right = TreeNode(6)

print(isValidBST(root2))  