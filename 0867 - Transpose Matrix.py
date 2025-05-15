class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        n = len(matrix)
        m = len(matrix[0])
        new_matrix = [[0 for _ in range(n)] for _ in range(m)]
        for j in range(m):
            for i in range(n):
                new_matrix[j][i] = matrix[i][j]
        return new_matrix