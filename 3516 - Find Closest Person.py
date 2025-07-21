class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        diff1, diff2 = abs(z - x), abs(z - y)
        if diff1 == diff2:
            return 0
        if diff1 > diff2:
            return 2
        if diff1 < diff2:
            return 1