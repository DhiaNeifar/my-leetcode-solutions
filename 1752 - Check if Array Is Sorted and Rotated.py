class Solution:
    def check(self, nums: List[int]) -> bool:
        if len(nums) < 2:
            return True
        rot = 0
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                rot = i + 1
                break
        for i in range(rot, rot + len(nums) - 1):
            index1 = i % len(nums)
            index2 = (i + 1) % len(nums)
            if nums[index1] > nums[index2]:
                return False
        return True