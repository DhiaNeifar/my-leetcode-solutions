class Solution:
    def longestPalindrome(self, s: str) -> str:
        length = len(s)
        curr = ''
        curr_length = 0
        for index in range(length * 2):
            if not index % 2:
                real_index = index // 2
                i, j = real_index, real_index
                while i >= 0 and j < length and s[i] == s[j]:
                    i -= 1
                    j += 1
                x = j - i - 1
                if curr_length < x:
                    curr = s[i + 1: j]
                    curr_length = x
            else:
                i, j = (index - 1) // 2, (index + 1) // 2
                while i >= 0 and j < length and s[i] == s[j]:
                    i -= 1
                    j += 1
                x = j - i - 1
                if curr_length < x:
                    curr = s[i + 1: j]
                    curr_length = x
        return curr