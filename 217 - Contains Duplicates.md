# 217 - Contains Duplicates

Difficulty: easy
Done: No
Last edited: February 24, 2022 12:13 AM

## Problem

Given an integer array `nums`, return `true` if any value appears **at least twice** in the array, and return `false` if every element is distinct.

## Solution

Naive solution would be to loop through all elements in array and comparing to the rest of the elements in the array, to see if *i* matches *j.* This would result in a O(N^2) solution since we are using performing N times for loop inside N time for loop. 

A better approach would be to run through the array just once, and using additional space to copy over traversed elements to a data structure. If *i* is already in our data structure we raise flag and break, without having to finish traversing all elements, since we only need 1 duplicate. 

## Code

```python
class Solution:  
    def containsDuplicate(self, nums: List[int]) -> bool:
        d = set()
        duplicates = False
        
        while not duplicates:
            for num in nums:
                if num not in d:
                    d.add(num)
                else: 
                    duplicates = True
            break
            
        return duplicates
```