class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        set1 = set(nums1)
        nums2.sort()
        set2 = set(nums2)
        return list(set1.intersection(set2))