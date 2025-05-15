class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        i, j = 0, 0
        s_new, t_new = "", "" 
        while i < len(s):
            if s[i] == '#':
                s_new = s_new[:-1]
            else: 
                s_new += s[i]
            i += 1
        while j < len(t):
            if t[j] == '#':
                t_new = t_new[:-1]
            else:
                t_new += t[j]
            j += 1
        return s_new == t_new