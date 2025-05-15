class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        total_sum = sum(nums)
        left_sum = 0
        splits = 0
        for num in nums:
            left_sum += num
            right_sum = total_sum - left_sum
            if left_sum >= right_sum:
                splits += 1
        if left_sum >= 0:
            splits -= 1
        return splits