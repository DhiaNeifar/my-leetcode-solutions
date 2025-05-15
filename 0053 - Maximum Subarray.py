class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sumlocal, sumglobal = nums[0], nums[0]
        for num in nums[1:]:
            sumlocal = max(num, sumlocal + num)
            sumglobal = max(sumlocal, sumglobal)
        return sumglobal