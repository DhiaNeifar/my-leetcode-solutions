class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)
        div = []
        for i in range(1, n // 2 + 1):
            if not n % i:
                div.append(i)
        for i in div:
            if s == s[:i] * (n // i):
                return True
        return False