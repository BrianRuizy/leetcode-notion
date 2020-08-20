# Given an array of integers nums.
# A pair (i,j) is called good if nums[i] == nums[j] and i < j.
# Return the number of good pairs.

# Example 1:
# Input: nums = [1,2,3,1,1,3]
# Output: 4
# Explanation: There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexed.

# Example 2:
# Input: nums = [1,1,1,1]
# Output: 6
# Explanation: Each pair in the array are good.

# Example 3:
# Input: nums = [1,2,3]
# Output: 0

# Constraints:
# 1 <= nums.length <= 100
# 1 <= nums[i] <= 100
from typing import List
from collections import Counter


class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        # list comprehension stores n of occurences of each value in nums
        occurences = [val for val in Counter(nums).values()]
        num_pairs = 0  # counter variable

        for val in occurences:
            if val > 1:  # can't make pair if number only occurs once
                # (n*(n–1)/2) pairs can be made with this n occurences
                num_pairs += val * (val-1)//2

        return num_pairs
