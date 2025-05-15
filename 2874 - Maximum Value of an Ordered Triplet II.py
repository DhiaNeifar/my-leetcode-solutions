class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        maxprefix = nums[0]
        maxdiff = 0
        result = 0
        for k in range(1, len(nums)):
            result = max(result, maxdiff * nums[k])
            maxdiff = max(maxdiff, maxprefix - nums[k])
            maxprefix = max(maxprefix, nums[k])
        return result