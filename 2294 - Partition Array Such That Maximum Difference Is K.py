class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        result = 0
        nums.sort()
        print(nums)
        i = 0
        while i < len(nums):
            j = i + 1
            while j < len(nums) and nums[j] - nums[i] <= k:
                j += 1
            result += 1
            i = j
        return result