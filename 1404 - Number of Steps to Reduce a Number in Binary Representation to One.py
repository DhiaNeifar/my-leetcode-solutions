class Solution:
    def numSteps(self, s: str) -> int:
        x = int(s, 2)
        count = 0
        while x != 1:
            if not x % 2:
                x //= 2
            else:
                x += 1
            count += 1
        return count