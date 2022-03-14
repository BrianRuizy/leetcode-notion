# 144 - Binary Tree Preorder Traversal

Difficulty: easy
Done: Yes
Last edited: March 13, 2022 10:59 PM
Link: https://leetcode.com/problems/binary-tree-preorder-traversal/
Topic: recursion, tree

## Problem

---

Given the `root` of a binary tree, return *the preorder traversal of its nodes' values*.

```
Input: root = [1,null,2,3]
Output: [1,2,3]
```

## Solution

---

Pre-order traversal requires order of parent -> left child -> right child. Can do so recursively, and return empty array if input is none

## Code

---

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        # if we have no nodes in input return empty list
        if not root: 
            return []
        
        # pre-order traversal requires order of parent -> left child -> right child
        # can do so recursively 
        
        return [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right)
```

## Time Complexity

---

The time complexity is O(n)*O*(*n*) because the recursive function is $T(n)=2⋅T(n/2)+1T(n)=2⋅T(n/2)+1$.