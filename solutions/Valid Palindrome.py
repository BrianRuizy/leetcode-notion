"""Given a string, determine if it is a palindrome, 
considering only alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.

Example 1:
Input: "A man, a plan, a canal: Panama"
Output: true

Example 2:
Input: "race a car"
Output: false

Constraints:
's' consists only of printable ASCII characters.
"""    
import re

class Solution:         
    def isPalindrome(self, s: str) -> bool:  
        # empty str is valid
        if not s:
            print('Empty string valid')
            return True
        
        elif s:
            # regex makes string alphanumeric, and drops underscores
            # to remove spaces and capitalize
            s = re.sub(r'[\W\_]', '', s) 
            s = s.upper().replace(' ', '')
            print(f'str: {s}')
            
            if s == s[::-1]:
                return True
            else:
                return False
