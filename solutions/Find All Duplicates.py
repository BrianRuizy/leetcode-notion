# Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

# Find all the elements that appear twice in this array.

# Could you do it without extra space and in O(n) runtime?

# Example:
# Input:
# [4,3,2,7,8,2,3,1]

# Output:
# [2,3]

from typing import List


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        my_dict = {}
        duplicates = []

        # traverse nums list linearly
        for x in nums:
            if x in my_dict:
                # if x is already in hash table, 
                # add x to duplicates list
                duplicates.append(x)
            else:
                # append every x value to hash table, if not already there
                # note: dictionary keys must be unique which aids our algorithm
                my_dict[x] = None

        return duplicates

# Runtime beats 96.27 % of python3 submissions!
