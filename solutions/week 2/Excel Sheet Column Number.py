class Solution:
    def titleToNumber(self, s: str) -> int:
        total = 0

        # Example:
        # s = 'CDA' --> ord(C)*26*26 + ord(D)*26 + ord(A) = 2133
        for exponent, letter in enumerate(s[::-1]):
            total += (ord(letter)-64)*26**exponent

        return total
