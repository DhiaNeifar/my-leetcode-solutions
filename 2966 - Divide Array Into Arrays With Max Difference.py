class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()
        results = [[] for _ in range(len(nums) // 3)]
        for i in range(len(nums)):
            results[i // 3].append(nums[i])
        for section in results:
            if section[2] - section[1] > k or section[1] - section[0] > k or section[2] - section[0] > k:
                return []
        return results