class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        for i in range(1, n):
            for j in range(n):
                first_index = max(0, j - 1)
                min_value = matrix[i - 1][first_index]
                for t in range(first_index + 1, min(j + 2, n)):
                    min_value = min(min_value, matrix[i - 1][t])
                matrix[i][j] += min_value
        return min(matrix[n - 1])