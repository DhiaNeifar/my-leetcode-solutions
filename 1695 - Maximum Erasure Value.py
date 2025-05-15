class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        nums_freq = {}
        
        right, left = 0, 0
        result = 0
        curr_sum = 0

        while right < len(nums):
            nums_freq[nums[right]] = nums_freq.get(nums[right], 0) + 1
            curr_sum += nums[right]
            
            while nums_freq[nums[right]] > 1:
                nums_freq[nums[left]] -= 1
                curr_sum -= nums[left]
                left += 1
            
            result = max(result, curr_sum)
            right += 1
        
        return result