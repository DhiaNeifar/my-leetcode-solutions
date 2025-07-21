class Solution:
    def findLHS(self, nums: List[int]) -> int:
        frequency = {}
        
        for num in nums:
            frequency[num] = frequency.get(num, 0) + 1
        
        result = 0
        for num in frequency:
            if num + 1 in frequency:
                result = max(result, frequency[num + 1] + frequency[num])
            
        return result