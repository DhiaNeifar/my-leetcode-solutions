class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        i = 1
        while i < len(nums) and nums[i - 1] % 2 != nums[i] % 2:
            i += 1
        return not i <= len(nums) - 1