class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        ordered_result = sorted(nums)[len(nums) - k:]
        result_dict = {}
        for num in ordered_result:
            result_dict[num] = result_dict.get(num, 0) + 1
        
        result = []
        
        for num in nums:
            if num in result_dict and result_dict[num] > 0:
                result.append(num)
                result_dict[num] -= 1
        
        return result