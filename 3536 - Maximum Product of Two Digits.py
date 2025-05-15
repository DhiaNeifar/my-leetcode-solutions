class Solution:
    def maxProduct(self, n: int) -> int:
        digits = []
        while n:
            n, rest = divmod(n, 10)
            digits.append(rest)
        digits.sort()
        return digits[-1] * digits[-2]