# 94 - Binary Tree Inorder Traversal

Difficulty: easy
Done: Yes
Last edited: March 13, 2022 10:05 PM
Link: https://leetcode.com/problems/binary-tree-inorder-traversal/
Topic: recursion, tree

## Problem

---

Given the `root` of a binary tree, return *the inorder traversal of its nodes' values*.

```
Input: root = [1,null,2,3]
Output: [1,3,2]
```

![Untitled](94%20-%20Binar%20a70d4/Untitled.png)

## Solution

---

in order traversal of binary tree requires to visit left child node parent node, then right child node, in that order. Will do so recursively, we know to print when node is a leaf node

## Whiteboard

---

![Untitled](94%20-%20Binar%20a70d4/Untitled%201.png)

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
    
    def __init__(self):
        self.res = []
    
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # in order traversal of binary tree requires to visit left child node, 
        # parent node, then right child node. In that order
        
        # will do so recursively
        # we know to print when node is a leaf node
        
        if root is None: 
            return []
        
        else: 
            return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)
```

## Time Complexity

---

The time complexity is O(n)*O*(*n*) because the recursive function is $T(n)=2⋅T(n/2)+1T(n)=2⋅T(n/2)+1$.