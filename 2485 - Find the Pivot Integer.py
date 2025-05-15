class Solution:
    def pivotInteger(self, n: int) -> int:
        x = n * (n + 1) // 2
        i = 1
        while i * i < x:
            i += 1
        if i * i == x:
            return i
        return -1