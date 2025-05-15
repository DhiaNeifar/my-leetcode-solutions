class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums)

        if len(nums) == 3:
            return max(nums[0] + nums[2], nums[1])

        dp = [0 for _ in nums]

        dp[0] = nums[0]
        dp[1] = nums[1]
        dp[2] = nums[2] + nums[0]

        for i in range(3, len(nums)):
            dp[i] = max(dp[i - 3], dp[i - 2]) + nums[i]

        return max(dp[-1], dp[-2])