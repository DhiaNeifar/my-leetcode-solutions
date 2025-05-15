class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        result = [[1], [1, 1]]
        for i in range(3, numRows + 1):
            new_row = [1 for _ in range(i)]
            for j in range(1, i - 1):
                new_row[j] = result[-1][j - 1] + result[-1][j]
            result.append(new_row)
        return result