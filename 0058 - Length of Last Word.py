class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        i = 0
        count = 0
        while i < len(s):
            while i < len(s) and s[i] == ' ':
                i += 1
            j = i
            while j < len(s) and s[j] != ' ':
                j += 1
            if j > i:
                count = j - i
            i = j
        return count