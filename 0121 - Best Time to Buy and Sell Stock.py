class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_list, max_list = [], []
        
        mi, ma = prices[0], prices[-1]
        result = 0
        for index, price in enumerate(prices):
            mi = min(mi, price)
            min_list.append(mi)

            ma = max(ma, prices[len(prices) - 1 - index])
            max_list.append(ma)

        for index, mi in enumerate(min_list):
            result = max(result, max_list[len(max_list) - 1 - index] - mi)

        return result