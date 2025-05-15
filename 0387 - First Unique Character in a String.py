class Solution:
    def firstUniqChar(self, s: str) -> int:
        frequency = {}
        for letter in s:
            frequency[letter] = frequency.get(letter, 0) + 1
        for index, letter in enumerate(s):
            if frequency[letter] == 1:
                return index
        return -1