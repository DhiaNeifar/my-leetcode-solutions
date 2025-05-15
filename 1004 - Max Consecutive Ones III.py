class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left, right = 0, 0
        longest_sequence = 0
        zeros = 0
        while right < len(nums):
            if nums[right] == 0:
                zeros += 1
            while zeros == k + 1:
                if nums[left] == 0:
                    zeros -= 1
                left += 1
            
            longest_sequence = max(longest_sequence, right - left + 1 )
            right += 1
        return longest_sequence