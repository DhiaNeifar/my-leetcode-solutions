from typing import List
from collections import defaultdict, deque


class Solution:
    def minMoves(self, matrix: List[str]) -> int:
        m, n = len(matrix), len(matrix[0])
        dist = [[float('inf')] * n for _ in range(m)]
        mp, u = defaultdict(list), set()

        for i in range(m):
            for j in range(n):
                c = matrix[i][j]
                if c.isupper():
                    mp[c].append((i, j))

        dq = deque()
        dq.appendleft((0, 0, 0))
        dist[0][0] = 0

        dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        while dq:
            x, y, d = dq.popleft()

            if x == m - 1 and y == n - 1:
                return d

            curr = matrix[x][y]
            if curr.isupper() and curr not in u:
                u.add(curr)
                for nx, ny in mp[curr]:
                    if dist[nx][ny] > d:
                        dist[nx][ny] = d
                        dq.appendleft((nx, ny, d))

            for dx, dy in dir:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and matrix[nx][ny] != '#':
                    if dist[nx][ny] > d + 1:
                        dist[nx][ny] = d + 1
                        dq.append((nx, ny, d + 1))

        return -1