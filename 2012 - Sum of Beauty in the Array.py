class Solution:
    def sumOfBeauties(self, nums: List[int]) -> int:
        n = len(nums)
        left_max = [0] * n
        right_min = [0] * n

        # Build left_max
        max_val = nums[0]
        for i in range(1, n):
            left_max[i] = max_val
            max_val = max(max_val, nums[i])

        # Build right_min
        min_val = nums[-1]
        for i in range(n - 2, -1, -1):
            right_min[i] = min_val
            min_val = min(min_val, nums[i])

        # Calculate beauty
        result = 0
        for i in range(1, n - 1):
            if left_max[i] < nums[i] < right_min[i]:
                result += 2
            elif nums[i - 1] < nums[i] < nums[i + 1]:
                result += 1

        return result