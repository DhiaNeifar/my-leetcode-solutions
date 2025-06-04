class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        zeros_position = []
        m, n = len(matrix), len(matrix[0])
        for row in range(m):
            for col in range(n):
                if not matrix[row][col]:
                    zeros_position.append((row, col))
        
        for row, col in zeros_position:
            for i in range(m):
                matrix[i][col] = 0
            for j in range(n):
                matrix[row][j] = 0