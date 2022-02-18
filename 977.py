class Solution:
    def sortedSquares(self, nums):
        left, right = 0, len(nums)-1

        stack = []

        while left <= right:
            max_abs = max(nums, key=abs)
            nums.remove(max_abs)
            stack.insert(0, abs(max_abs)**2)
            left += 1
        
        return stack


if __name__ == '__main__':
    s = Solution()
    s.sortedSquares(nums = [-3, -3, 0,0, 1, 10])
