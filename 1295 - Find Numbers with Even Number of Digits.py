class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        result = 0
        for num in nums:
            number_digits = 0
            while num:
                num //= 10
                number_digits += 1
            if number_digits % 2 == 0:
                result += 1
        return result