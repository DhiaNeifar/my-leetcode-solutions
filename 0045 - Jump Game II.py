class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        dp = [len(nums) for _ in nums]
        dp[0] = 0
        for index, num in enumerate(nums):
            j = index + 1
            while j < len(dp) and j <= index + num:
                dp[j] = min(dp[j], dp[index] + 1)
                j += 1
        return dp[-1]