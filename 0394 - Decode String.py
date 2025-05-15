class Solution:
    def decodeString(self, s: str) -> str:
        i = 0
        while i < len(s):
            if s[i].isdigit():
                k = i + 1
                while s[i: k + 1].isdigit():
                    k += 1
                integer = int(s[i: k])
                k = k - 1
                j = k + 2
                x = 1
                while j < len(s) and x != 0:
                    if s[j] == '[':
                        x += 1
                    if s[j] == ']':
                        x -= 1
                    j += 1
                s = s[:i] + s[k + 2: j - 1] * integer + s[j:]
            else:
                i += 1
        return s