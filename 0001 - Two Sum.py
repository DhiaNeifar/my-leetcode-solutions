class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        our_map = {}
        for index, num in enumerate(nums):
            difference = target - num
            if difference in our_map:
                return [our_map[difference], index]
            our_map[num] = index