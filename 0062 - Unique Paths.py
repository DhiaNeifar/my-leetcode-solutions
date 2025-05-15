class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m == n == 1:
            return 1
        grid = [[1 for _ in range(m)] for _ in range(n)]
        grid[0][0] = 0
        for i in range(1, m):
            for j in range(1, n):
                grid[j][i] = grid[j][i - 1] + grid[j - 1][i]
        return grid[n - 1][m - 1]