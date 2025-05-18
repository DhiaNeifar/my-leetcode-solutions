class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        l = [[] for _ in range(numRows)]
        i = 0

        while i < len(s):
            j = 0
            while j < numRows and i + j < len(s):
                l[j].append(s[i + j])
                j += 1
            i += numRows
            j = 1
            while j < numRows - 1 and i + j - 1 < len(s):
                l[numRows - j - 1].append(s[i + j - 1])
                j += 1
            i += numRows - 2
        return "".join(["".join(word) for word in l])