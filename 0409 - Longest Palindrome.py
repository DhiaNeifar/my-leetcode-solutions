class Solution:
    def longestPalindrome(self, s: str) -> int:
        frequency = {}
        for char in s:
            x = frequency.get(char, 0)
            frequency[char] = x + 1
        count, a = 0, 0
        for value in frequency.values():
            if value % 2:
                count += value - 1
                a = 1
            else:
                count += value
        return count + a