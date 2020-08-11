from string import ascii_uppercase


class Solution:
    def titleToNumber(self, s: str) -> int:
        # converting string to list
        s = list(s)
        total = 0

        # hash letters to base 26 value
        az_map = dict(zip(ascii_uppercase, [i for i in range(1, 27)]*26))

        # Perform base case arithmetic for each value
        # Example: using letter for dict key
        # s = 'CDA' --> az_map[C]*26*26 + az_map[D]*26 + az_map[A]
        for exponent, letter in enumerate(s[::-1]):
            total += az_map[letter]*26**exponent

        return total
