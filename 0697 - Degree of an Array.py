class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        degree = 0

        result = len(nums)
        for key, value in freq.items():
            degree = max(value, degree)
        
        for key, value in freq.items():
            if(value == degree):
                first_index = len(nums)
                last_index = -1
                for index, num in enumerate(nums):
                    if num == key:
                        first_index = min(first_index, index)
                        last_index = max(last_index, index)  
                result = min(result, last_index - first_index + 1)
        return result