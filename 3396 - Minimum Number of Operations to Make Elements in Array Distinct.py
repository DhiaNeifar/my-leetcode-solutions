class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        x, y = len(nums) % 3, len(nums) // 3
        our_set = set()
        if x == 1:
            our_set.add(nums[-1])
        if x == 2:
            our_set.add(nums[-1])
            if nums[-2] in our_set:
                return y + 1
            our_set.add(nums[-2])
        while y:
            for j in range(y * 3 - 1, (y - 1) * 3 - 1, -1):
                if nums[j] in our_set:
                    return y
                else:
                    our_set.add(nums[j])
            y -= 1
        return 0