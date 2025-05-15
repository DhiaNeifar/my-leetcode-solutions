class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        if len(s) >= 2:
            _max = -1
            i = 0
            while i < len(s) - 1:
                j = len(s) - 1
                while s[i] != s[j] and j > i:
                    j -= 1
                _max = max(_max, j - i - 1)
                i += 1
            return _max
        return -1