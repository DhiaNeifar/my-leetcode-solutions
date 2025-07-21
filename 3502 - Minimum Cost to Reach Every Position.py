class Solution:
    def minCosts(self, cost: List[int]) -> List[int]:
        curr_min = cost[0]
        result = [curr_min]
        for i in range(1, len(cost)):
            curr_min = min(curr_min, cost[i])
            result.append(curr_min)
        return result