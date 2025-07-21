class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        result = inf
        for i in range(len(nums) - 2):
            for j in range(i + 1, len(nums) - 1):
                if nums[i] < nums[j]: 
                    for k in range(j + 1, len(nums)):
                        if nums[k] < nums[j]:
                            result = min(result, nums[i] + nums[j] + nums[k])
        return -1 if result == inf else result