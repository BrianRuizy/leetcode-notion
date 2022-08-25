# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



class Solution:
    def invertTree(self, root) -> Optional[TreeNode]:
        # do if root is not null
        if root:
            self.invertTree(root.left)
            self.invertTree(root.right)
            
            root.left, root.right = root.right, root.left
        
        return root

 
if '__name__' == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    
    sol = Solution()
    sol.invertTree(root)