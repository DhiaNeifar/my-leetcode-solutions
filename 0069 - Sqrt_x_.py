class Solution:
    def mySqrt(self, x: int) -> int:
        a, b, n = 0, 1, 0
        while a + b <= x:
            n += 1
            a += b
            b += 2
        return n