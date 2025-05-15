class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        def func(x):
            if x < 0:
                return 0
            result = 0
            l = 0
            curr, r = 0, 0
            for r in range(l, len(nums)):
                curr += nums[r]
                while curr > x:
                    curr -= nums[l]
                    l += 1
                result += r - l + 1
            return result

        return func(goal) - func(goal - 1)