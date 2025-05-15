class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        if s:
            g.sort()
            s.sort()
            i, j = 0, 0
            while j < len(s) and i < len(g):
                if s[j] >= g[i]:
                    i += 1
                j += 1
            return i
        return 0