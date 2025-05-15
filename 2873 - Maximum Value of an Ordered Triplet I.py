class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        i = 0
        max_ = 0
        while i < len(nums) - 2:
            j = i + 1
            while j < len(nums) - 1:
                k = j + 1
                while k < len(nums):
                    max_ = max((nums[i] - nums[j]) * nums[k], max_)
                    k += 1
                j += 1
            i += 1   
        return max_ if max_ > 0 else 0