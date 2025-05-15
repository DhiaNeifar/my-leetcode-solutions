class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        n = len(grid)
        result = 0
        for i in range(n):
            row = grid[i]
            for j in range(n):
                column = []
                for k in range(n):
                    column.append(grid[k][j])
                if row == column:
                    result += 1
        return result