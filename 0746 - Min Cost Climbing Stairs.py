class Solution:
    def minCostClimbingStairs(self, costs: List[int]) -> int:
        x, y = 0, 0
        for cost in costs:
            temp = min(x + cost, y + cost)
            x = y
            y = temp
        return min(x, y)