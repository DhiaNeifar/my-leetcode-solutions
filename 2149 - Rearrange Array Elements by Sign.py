class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        results = []
        i, j = 0, 0
        while i < len(nums) and j < len(nums):
            while nums[i] < 0:
                i += 1
            while nums[j] > 0:
                j += 1
            results.append(nums[i])
            results.append(nums[j])
            i += 1
            j += 1
        return results