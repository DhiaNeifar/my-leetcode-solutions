class Solution:
    def numberOfSteps(self, num: int) -> int:
        operations = 0
        while num:
            if num % 2:
                num -= 1
            else:
                num //= 2
            operations += 1
        return operations