class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n % 2:
            return pow(x, n - 1) * x
        else:
            a = pow(x, n // 2)
            return a * a