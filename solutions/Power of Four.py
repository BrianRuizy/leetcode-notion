from math import log
class Solution:
    def isPowerOfFour(self, num: int) -> bool:        
        # True if num is not 0, AND log₄(num) is a whole-number
        return num > 0 and log(num, 4).is_integer()