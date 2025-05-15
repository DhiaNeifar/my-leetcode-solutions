class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        def check_notdistinct(dictionary):
            for element in dictionary.values():
                if element > 1:
                    return True
            return False
        freq_dict = {}
        for num in nums:
            freq_dict[num] = freq_dict.get(num, 0) + 1
        operations = 0
        while freq_dict and check_notdistinct(freq_dict):
            for element in range(operations * 3, min(len(nums), (operations + 1) * 3)):
                freq_dict[nums[element]] -= 1
                if freq_dict[nums[element]] == 0:
                    freq_dict.pop(nums[element])
            operations += 1
        return operations