from string import ascii_uppercase


class Solution:
    def titleToNumber(self, s: str) -> int:
        total = 0

        # hash letters to base 26 value
        az_map = dict(zip(ascii_uppercase, [i for i in range(1, 27)]*26))

        # Example:
        # s = 'CDA' --> az_map[C]*26*26 + az_map[D]*26 + az_map[A]
        for exponent, letter in enumerate(s[::-1]):
            total += az_map[letter]*26**exponent

        return total
