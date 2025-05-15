class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        length_count = 6
        count = [0 for _ in range(length_count)]
        for i in range(len(tops)):
            count[tops[i] - 1] += 1
            count[bottoms[i] - 1] += 1
        trump = 0
        max_count = 0
        for i in range(length_count):
            if max_count < count[i]:
                max_count = count[i]
                trump = i + 1
        if max_count < len(tops):
            return -1
        tops_operations = 0
        for i in range(len(tops)):
            if tops[i] != trump and bottoms[i] != trump:
                return -1
            if tops[i] != trump and bottoms[i] == trump:
                tops_operations += 1
        bottoms_operations = 0
        for i in range(len(tops)):
            if bottoms[i] != trump and tops[i] != trump:
                return -1
            if bottoms[i] != trump and tops[i] == trump:
                bottoms_operations += 1

        return min(tops_operations, bottoms_operations)