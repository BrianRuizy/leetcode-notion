# Given a non-negative index k where k ≤ 33, return the kth index row of the Pascal's triangle.

# Note that the row index starts from 0.
# In Pascal's triangle, each number is the sum of the two numbers directly above it.

# Example:
# Input: 3
# Output: [1,3,3,1]
# Follow up:

# Could you optimize your algorithm to use only O(k) extra space?
from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[List[int]]:
        if rowIndex == 1:
            return [1, 1]

        elif rowIndex == 2:
            return [1, 2, 1]

        else:
            triangle = [[1], [1, 1]]
            for i in range(1, rowIndex):
                current_row = [1]
                j = 0
                while j < i:
                    current_row.append(triangle[i][j] + triangle[i][j+1])
                    j += 1

                current_row.append(1)
                triangle.append(current_row)

            return triangle[rowIndex]
