class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        if len(nums) == 1:
            return [nums]
        
        nums.sort()
        result = []
        for i in range(0, len(nums), 3):
            if nums[i + 2] - nums[i] > k:
                return []
            result.append([nums[i + j] for j in range(3)])
        return result