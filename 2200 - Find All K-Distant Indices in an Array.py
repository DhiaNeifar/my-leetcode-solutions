class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        our_set = set()
        for index, num in enumerate(nums):
            if num == key:
                for i in range(max(0, index - k), min(len(nums), index + k + 1)):
                    our_set.add(i)
        
        return list(our_set)