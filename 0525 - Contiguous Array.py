class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        tracker = {}
        tracker[0] = -1
        maxlen = 0
        count = 0
        for i in range(len(nums)):
            count += 1 if nums[i] == 1 else -1
            x = tracker.get(count, 0)
            if count in tracker:
                maxlen = max(maxlen, i - tracker[count])
            else:
                tracker[count] = i
        return maxlen