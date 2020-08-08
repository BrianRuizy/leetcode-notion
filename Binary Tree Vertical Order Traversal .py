# Given a binary tree, return the vertical order traversal of its nodes values.
# For each node at position (X, Y), its left and right children respectively will be at positions (X-1, Y-1) and (X+1, Y-1).
# Running a vertical line from X = -infinity to X = +infinity, whenever the vertical line touches some nodes, 
# we report the values of the nodes in order from top to bottom (decreasing Y coordinates).
# If two nodes have the same position, then the value of the node that is reported first is the value that is smaller.
# Return an list of non-empty reports in order of X coordinate.  Every report will have a list of values of nodes.

from collections import defaultdict

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        pass