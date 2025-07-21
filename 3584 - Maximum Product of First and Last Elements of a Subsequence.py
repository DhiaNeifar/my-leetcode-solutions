class Solution:
    def maximumProduct(self, nums: List[int], m: int) -> int:
        ma = mi = nums[0]
        res = -inf
        for i in range(m - 1, len(nums)):
            ma = max(ma, nums[i - m + 1])
            mi = min(mi, nums[i - m + 1])
            res = max(res, mi * nums[i], ma * nums[i])
        
        return res