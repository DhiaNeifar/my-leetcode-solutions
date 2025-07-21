class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1 or nums[0] < nums[-1]:
            return nums[0]
        r, l = 0, len(nums) - 1
        while r < l and nums[r] > nums[l]:
            r += 1
            l -= 1
        return min(nums[r - 1], nums[r], nums[l], nums[l + 1])