class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zeros, ones = 0, 0
        for num in nums:
            if num == 0:
                zeros += 1
            if num == 1:
                ones += 1
        for i in range(zeros):
            nums[i] = 0
        for i in range(zeros, zeros + ones):
            nums[i] = 1
        for i in range(zeros + ones, len(nums)):
            nums[i] = 2