class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        def CheckUpBorders(table, row, column):
            up_range = 0
            for k in range(1, table[row - 1][column - 1] + 1):
                if table[row - k][column] == 0:
                    break
                up_range += 1
            return up_range

        def CheckLeftBorders(table, row, column):
            left_range = 0
            for k in range(1, table[row - 1][column - 1] + 1):
                if table[row][column - k] == 0:
                    break
                left_range += 1
            return left_range

        m, n = len(matrix), len(matrix[0])
        dp = [[int(matrix[i][j]) for j in range(n)] for i in range(m)]
        result = 0
        for j in range(n):
            if dp[0][j] == 1:
                result = 1
                break

        for i in range(m):
            if dp[i][0] == 1:
                result = 1
                break

        for i in range(1, m):
            for j in range(1, n):
                result = max(result, dp[i][j])
                if dp[i][j] and dp[i - 1][j - 1]:
                    dp[i][j] += min(CheckUpBorders(dp, i, j), CheckLeftBorders(dp, i, j))
                    result = max(result, dp[i][j])
        return result * result