class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        min_, max_ = nums[0], nums[0]
        freq = {}
        for num in nums:
            min_ = min(min_, num)
            max_ = max(max_, num)
            freq[num] = freq.get(num, 0) + 1
        
        table = [0] * (max_ - min_ + 1)
        for num in freq:
            table[num - min_] = freq[num] * num
        
        if len(table) == 1:
            return table[0]
        
        if len(table) == 2:
            return max(table)
        
        if len(table) == 3:
            return max(table[0] + table[2], table[1])

        dp = [0] * len(table)
        dp[0] = table[0]
        dp[1] = table[1]
        dp[2] = table[2] + table[0]
        for i in range(3, len(table)):
            dp[i] = max(dp[i - 2], dp[i - 3]) + table[i]
        
        return max(dp[-1], dp[-2])