class Solution:
    def fib(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 0:
            return 0
        
        n1, n2 = 0, 1
        n3 = n1 + n2
        while n - 2:
            n1, n2 = n2, n3
            n3 = n1 + n2
            n -= 1
        return n3