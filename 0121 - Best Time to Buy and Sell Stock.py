class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        stack = []
        max_profit = 0
        for price in prices:
            while stack and stack[-1] > price:
                stack.pop()
            if stack:
                max_profit = max(price - stack[-1], max_profit)
            else:
                stack.append(price)
        return max_profit