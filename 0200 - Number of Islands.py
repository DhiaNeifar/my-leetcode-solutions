class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        result = 0
        adjacents = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        visited = [[False for _ in range(n)] for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if not visited[i][j] and grid[i][j] == "1":
                    result += 1
                    queue = deque([(i, j)])
                    while queue:
                        curr_position = queue.popleft()
                        x, y = curr_position[0], curr_position[1]
                        for dx, dy in adjacents:
                            if 0 <= dx + x < m and 0 <= dy + y < n and grid[dx + x][dy + y] == "1" and not visited[dx + x][dy + y]:
                                queue.append((dx + x, dy + y))
                                visited[dx + x][dy + y] = True
        
        return result