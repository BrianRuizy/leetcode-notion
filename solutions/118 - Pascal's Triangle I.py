# 118. Pascal's Triangle
# Easy
# Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.
# In Pascal's triangle, each number is the sum of the two numbers directly above it.

# Example:
# Input: 5
# Output:
# [
#      [1],
#     [1,1],
#    [1,2,1],
#   [1,3,3,1],
#  [1,4,6,4,1]
# ]
from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1 or numRows < 0:
            return [[1]]

        elif numRows == 2:
            return [[1], [1, 1]]

        else:
            triangle = [[1], [1, 1]]
            for i in range(1, numRows-1):
                current_row = [1]
                j = 0
                while j < i:
                    current_row.append(triangle[i][j] + triangle[i][j+1])
                    j += 1

                current_row.append(1)
                triangle.append(current_row)

            return triangle[numRows - 1]
