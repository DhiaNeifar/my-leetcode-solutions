class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        l_s, l_t = [], []
        for char in s:
            if char == "#" and not l_s:
                continue
            if char == "#" and l_s:
                l_s.pop()
            else:
                l_s.append(char)
        
        for char in t:
            if char == "#" and not l_t:
                continue
            if char == "#" and l_t:
                l_t.pop()
            else:
                l_t.append(char)
        
        return l_s == l_t