# 145 - Binary Tree Postorder Traversal

Difficulty: easy
Done: Yes
Last edited: March 13, 2022 10:59 PM
Link: https://leetcode.com/problems/binary-tree-postorder-traversal/
Topic: recursion, tree

## Problem

---

Given the `root` of a binary tree, return *the preorder traversal of its nodes' values*.

```
Input: root = [1,null,2,3]
Output: [3,2,1]
```

## Solution

---

post order goes as left child -> right child -> root

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
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        return self.postorderTraversal(root.left) + self.postorderTraversal(root.right) + [root.val] if  root is not None else []
```

## Time Complexity

---

The time complexity is O(n)*O*(*n*) because the recursive function is $T(n)=2⋅T(n/2)+1T(n)=2⋅T(n/2)+1$.