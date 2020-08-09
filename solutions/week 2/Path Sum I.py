# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        result = []
        self.depthFirstSearch(root, sum, result)
        return any(result)  # Returns true if True in iterable

    def depthFirstSearch(self, root, sum, result):
        # pre-order DFS recursive traversal

        if not root:
            return False

        # Traverse until no child nodes; not root.L && not root.R
        if not root.left and not root.right:
            if root.val == sum:
                result.append(True)

        if root.left:
            self.depthFirstSearch(root.left, sum-root.val, result)

        if root.right:
            self.depthFirstSearch(root.right, sum-root.val, result)
