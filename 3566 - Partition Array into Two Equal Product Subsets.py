class Solution:
    def checkEqualPartitions(self, nums: List[int], target: int) -> bool:
        if len(nums) < 3:
            return False
        product = 1
        for num in nums:
            product *= num
        if product == target * target:
            return True
        return False