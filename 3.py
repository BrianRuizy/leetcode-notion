class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # sliding window approach requiring two pointers
        # set variable containing all unique 
        left = 0
        right = 0
        longest = 0
        charset = set()

        for right in range(len(s)):
            while s[right] in charset:
                # look for duplicate
                charset.remove(s[left])
                left += 1
            
            charset.add(s[right])
            if len(charset) > longest:
                longest = len(charset)
        
        return longest


if __name__ == '__main__':
    obj = Solution()
    obj.lengthOfLongestSubstring(s = "abcabcbb")
         