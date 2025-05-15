class Solution:
    def isValid(self, s: str) -> bool:
        l = []
        for p in s:
            if p in ['{', '(', '[']:
                l.append(p)
            else:
                if l and ((p == '}' and l[-1] == '{') or (p == ']' and l[-1] == '[') or (p == ')' and l[-1] == '(')):
                    l.pop()
                else:
                    return False
        
        if len(l):
            return False
        return True