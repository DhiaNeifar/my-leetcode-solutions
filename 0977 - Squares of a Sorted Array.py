class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        results = []
        i, j = 0, len(nums) - 1
        while i <= j:
            if abs(nums[i]) < abs(nums[j]):
                results.append(nums[j] * nums[j])
                j -= 1
            else:
                results.append(nums[i] * nums[i])
                i += 1
        return results[::-1]