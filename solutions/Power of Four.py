from math import log

class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        if num <= 0:
            return False
        
        # if argument num is a whole number then True
        # else not a power of 4
        return log(num, 4).is_integer()