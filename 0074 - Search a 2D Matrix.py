class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        l = [matrix[i][j] for i in range(m) for j in range(n)]

        start = 0
        end = m * n - 1
        while start <= end:
            mid = start + (end - start) // 2
            if l[mid] == target:
                return True
            if l[mid] < target:
                start = mid + 1
            if target < l[mid]:
                end = mid - 1
        return False