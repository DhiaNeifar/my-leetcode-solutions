class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        result = -1
        curr_min = nums[0]
        for num in nums:
            if num > curr_min:
                result = max(result, num - curr_min)
            curr_min = min(curr_min, num)
        return result