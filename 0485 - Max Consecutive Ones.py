class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        consecutives = [0] * (len(nums) + 1)
        max_consecutive = 0
        for index, num in enumerate(nums):
            if num:
                consecutives[index + 1] = consecutives[index] + 1
                max_consecutive = max(max_consecutive, consecutives[index + 1])
            else:
                consecutives[index] = 0
        return max_consecutive