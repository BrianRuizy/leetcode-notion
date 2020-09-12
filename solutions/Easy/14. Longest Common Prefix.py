class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # traverse smallest word in list
        # traverse all words in list
        # if letter in word does not equal the current letter of smallest word
        # return current word sliced up to the current index of smallest word
        if not strs:
            return ''

        smallest = min(strs, key=len)
        for index, char in enumerate(smallest):
            for word in strs:
                if word[index] != char:
                    return smallest[:index]

        # finally return smallest
        return smallest
