class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        mapper = {num: i for i, num in enumerate(nums2)}
        return [mapper[num] for num in nums1]