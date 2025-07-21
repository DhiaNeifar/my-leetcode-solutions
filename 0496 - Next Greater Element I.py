class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = [-1 for _ in nums1]
        for ind1, num1 in enumerate(nums1):
            i = 0
            while nums2[i] != num1:
                i += 1
            for j in range(i + 1, len(nums2)):
                if nums2[j] > num1:
                    result[ind1] = nums2[j]
                    break
        return result