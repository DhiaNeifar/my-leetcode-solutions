class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        our_set = set()
        for num in nums:
            if num < k:
                return -1
            if num != k:
                our_set.add(num)
        return len(our_set)