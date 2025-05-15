class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i, k = 0, 0
        while i < len(nums):
            if nums[i] == val:
                k += 1
            else:
                nums[i - k] = nums[i]
            i += 1
        return i - k