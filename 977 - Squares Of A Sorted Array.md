# 977 - Squares Of A Sorted Array

Difficulty: easy
Done: No
Last edited: February 17, 2022 12:47 PM
Topic: two pointers

## Problem

Given an integer array `nums` sorted in **non-decreasing** order, return *an array of **the squares of each number** sorted in non-decreasing order*.

Example 1:

```
Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].

```

Example 2:

```
Input: nums = [-7,-3,2,3,11]
Output: [4,9,9,49,121]

```

Constraints:

- `1 <= nums.length <= 104`
- `104 <= nums[i] <= 104`
- `nums` is sorted in **non-decreasing** order.

## Solution

lorem ipsum

## Whiteboard

[http://excalidraw.com](http://excalidraw.com)

## Code

```python
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        return sorted([x**2 for x in nums])
```

using built-in sorted

```python
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left, right = 0, len(nums)-1

        while left <= right:
            
            max_abs = max(nums[left:], key=abs)
            
            nums.insert(0, nums.pop(nums.index(max_abs)))
            nums[0] = nums[0]**2
            left += 1
        
        return nums
```

custom 2 pointer approach
