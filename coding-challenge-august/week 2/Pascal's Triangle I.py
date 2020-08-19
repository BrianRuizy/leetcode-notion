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
