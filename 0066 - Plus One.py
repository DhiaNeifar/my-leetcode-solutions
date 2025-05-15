class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digit = 0
        ten = 1
        l = []
        for i in range(len(digits) - 1, -1, -1):
            digit += digits[i] * ten
            ten *= 10
        digit += 1
        if digit // ten == 0:
            ten //= 10
        while ten:
            l.append(digit // ten)
            digit %= ten
            ten //= 10
        return l