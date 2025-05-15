class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        zeros = 0
        while i + zeros < len(nums):
            if nums[i + zeros] == 0:
                zeros += 1
            else:
                nums[i] = nums[i + zeros]
                i += 1
        while i < len(nums):
            nums[i] = 0
            i += 1