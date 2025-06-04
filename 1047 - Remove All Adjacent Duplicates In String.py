class Solution:
    def removeDuplicates(self, s: str) -> str:
        l = []
        for char in s:
            if l and l[-1] == char:
                l.pop()
            else:
                l.append(char)
        return "".join(l)