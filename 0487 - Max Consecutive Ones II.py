class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        longest_sequence = 0
        left, right = 0, 0
        zeros = 0
        
        while right < len(nums):
            if nums[right] == 0:
                zeros += 1
            
            while zeros == 2:
                if nums[left] == 0:
                    zeros -= 1
                left += 1

            longest_sequence = max(longest_sequence, right - left + 1)
            right += 1
        
        return longest_sequence