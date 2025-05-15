class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 1
        element = nums[0]
        i = 1
        while i < len(nums):
            if nums[i] == element:
                count += 1
            else:
                if count > 1:
                    count -= 1
                else:
                    element = nums[i]
                    count = 1
            i += 1
        return element