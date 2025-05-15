class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        count = [0 for _ in range(len(nums) + 1)]
        duplicated = 0
        for i in range(len(nums)):
            if count[nums[i]] == 1:
                duplicated = nums[i]
            count[nums[i]] = 1
        i = 1
        while count[i]:
            i += 1
        return [duplicated, i]