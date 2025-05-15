class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        output = -1
        i = 0
        while i <= len(haystack) - len(needle):
            v, j = 1, 0
            while j < len(needle) and v:
                if needle[j] != haystack[i + j]:
                    v = 0
                    break
                j += 1
            if v:
                return i
            i += 1
        return output