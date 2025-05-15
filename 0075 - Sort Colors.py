class Solution:
    def sortColors(self, nums: List[int]) -> None:
        if not nums:
            return []
        
        length = len(nums)
        r, w = 0, 0
        for i in range (length):
            if nums[i] == 0:
                r += 1
            elif nums[i] == 1:
                w += 1
        
        for i in range (r):
            nums[i] = 0
        for i in range (r, r + w):
            nums[i] = 1
        for i in range (r + w, length ):
            nums[i] = 2
        """
        Do not return anything, modify nums in-place instead.
        """