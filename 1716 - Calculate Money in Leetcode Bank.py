class Solution:
    def totalMoney(self, n: int) -> int:
        div = n // 7
        rest = n % 7
        sum_ = rest * (rest + 1) // 2 
        return sum_ + div * rest + 28 * div + 7 * div * (div - 1) // 2