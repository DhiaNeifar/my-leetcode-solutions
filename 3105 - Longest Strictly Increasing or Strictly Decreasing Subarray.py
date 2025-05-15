class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1
        MaximumLength = 0
        increasing, decreasing = 1, 1
        i = 0
        while i < len(nums) - 1:
            if nums[i] < nums[i + 1]:
                increasing += 1
                decreasing = 1
            if nums[i + 1] < nums[i]:
                increasing = 1
                decreasing += 1
            if nums[i] == nums[i + 1]:
                increasing = 1
                decreasing = 1
            MaximumLength = max(MaximumLength, max(increasing, decreasing))
            i += 1
        return MaximumLength