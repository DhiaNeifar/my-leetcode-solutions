class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        right, left = 0, 0
        result = 0
        count = {}
        while right < len(nums):
            count[nums[right]] = count.get(nums[right], 0) + 1
            
            while count[nums[right]] > k:
                count[nums[left]] -= 1
                left += 1
            
            result = max(result, right - left + 1)
            
            right += 1
        
        return result