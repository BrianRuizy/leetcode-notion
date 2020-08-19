from collections import defaultdict


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def pathSum(self, root, sum):
        self.result, self.count = 0, defaultdict(int)
        self.count[sum] = 1
        self.depthFirstSearch(root, sum, 0)
        return self.result

    def depthFirstSearch(self, root, sum, root_sum):
        if not root:
            return None

        root_sum += root.val
        self.result += self.count[root_sum]
        self.count[root_sum + sum] += 1
        self.depthFirstSearch(root.left, sum, root_sum)
        self.depthFirstSearch(root.right, sum, root_sum)
        self.count[root_sum + sum] -= 1
