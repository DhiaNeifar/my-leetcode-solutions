class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        asc, desc = False, False
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:    
                asc = True
            if nums[i] < nums[i - 1]:
                desc = True
        return not (asc and desc)