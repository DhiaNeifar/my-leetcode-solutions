class Solution:
    def minAbsDiff(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        
        result = [[0 for _ in range(n - k + 1)] for _ in range(m - k + 1)]

        if k == 1:
            return result
        
        for row in range(m - k + 1):
            for col in range(n - k + 1):
                curr_submatrix = set()
                for i in range(k):
                    for j in range(k):
                        curr_submatrix.add(grid[row + i][col + j])
                if len(curr_submatrix) == 1:
                    result[row][col] = 0
                else:
                    curr_submatrix = list(curr_submatrix)
                    curr_submatrix.sort()
                    minimum = abs(curr_submatrix[1] - curr_submatrix[0])
                    for i in range(2, len(curr_submatrix)):
                        minimum = min(minimum, abs(curr_submatrix[i] - curr_submatrix[i - 1]))        
                    result[row][col] = minimum
        return result