class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        totalsum = sum(nums)
        target, remainder = divmod(totalsum, 2)
        if remainder:
            return False
        
        our_set = {0}
        for num in nums:
            next_set = our_set.copy()
            for element in our_set:
                result = num + element
                if result == target:
                    return True
                next_set.add(result)
            our_set = next_set
        return False