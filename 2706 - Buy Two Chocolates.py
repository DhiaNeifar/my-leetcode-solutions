class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        prices.sort()
        rest = prices[0] + prices[1]
        if prices[0] >= money or rest > money:
            return money
        return money - rest