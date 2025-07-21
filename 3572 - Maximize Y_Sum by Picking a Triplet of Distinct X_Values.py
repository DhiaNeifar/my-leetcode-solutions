class Solution:
    def maxSumDistinctTriplet(self, x: List[int], y: List[int]) -> int:
        freq = {}
        for index, val in enumerate(x):
            freq[val] = max(y[index], freq.get(val, 0))
        
        if len(freq) < 3:
            return -1
        
        values = list(freq.values())
        values.sort()
        return values[-1] + values[-2] + values[-3]