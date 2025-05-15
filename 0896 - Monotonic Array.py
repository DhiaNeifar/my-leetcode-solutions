class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return True
        i = 1
        while i < len(nums) and nums[i] == nums[i - 1]:
            i += 1
        if i == len(nums):
            return True
        if nums[i] > nums[i - 1]:
            for j in range(i + 1, len(nums)):
                if nums[j] < nums[j - 1]:
                    return False
        if nums[i] < nums[i - 1]:
            for j in range(i + 1, len(nums)):
                if nums[j] > nums[j - 1]:
                    return False
        return True