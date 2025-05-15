class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid[0]), len(grid)
        for i in range(1, m):
            grid[0][i] = grid[0][i - 1] + grid[0][i]
        for j in range(1, n):
            grid[j][0] = grid[j - 1][0] + grid[j][0]
        for i in range(1, m):
            for j in range(1, n):
                grid[j][i] = min(grid[j][i - 1], grid[j - 1][i]) + grid[j][i]
        return grid[-1][-1]