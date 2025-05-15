class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        i, j = 0, 0
        m , n = len(nums1), len(nums2)
        nums3 = []
        while i < m and j < n and (i + j) < (((n + m) // 2) + 1):
            if nums1[i] < nums2[j]:
                nums3.append(nums1[i])
                i += 1
            else: 
                nums3.append(nums2[j])
                j += 1
        while i < m and i + j < (((n + m) // 2) + 1):
            nums3.append(nums1[i])
            i += 1
        while j < n and i + j < (((n + m) // 2) + 1):
            nums3.append(nums2[j])
            j += 1
        if (n + m) % 2:
            return  nums3[-1]
        else: 
            return (nums3[-1] + nums3[-2]) / 2