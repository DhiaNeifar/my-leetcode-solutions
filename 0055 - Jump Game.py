class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        if len(nums) > 1 and nums[0] == 0:
            return False

        max_index = nums[0]
        i = 1
        i = 1
        while i <= max_index and i < len(nums):
            max_index = max(max_index, i + nums[i])
            i += 1
        return max_index >= len(nums) - 1