import heapq
from typing import List

class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        n, m = len(moveTime), len(moveTime[0])
        graph = ConstructGraph(moveTime, n, m)

        distances = {node: float('inf') for node in graph}
        distances[0] = 0

        heap = [(0, 0)]  # (time, node)

        while heap:
            curr_time, u = heapq.heappop(heap)

            if curr_time > distances[u]:
                continue

            for v, wait_time in graph[u]:
                # compute 2D coordinates to index moveTime
                x, y = v // m, v % m
                arrival_time = max(curr_time, moveTime[x][y]) + 1

                if arrival_time < distances[v]:
                    distances[v] = arrival_time
                    heapq.heappush(heap, (arrival_time, v))

        target = m * (n - 1) + (m - 1)
        return distances[target]

def ConstructGraph(moveTime: List[List[int]], n: int, m: int) -> dict:
    graph = {}
    for i in range(n):
        for j in range(m):
            u = m * i + j
            adjacent = []
            for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
                ni, nj = i + dx, j + dy
                if 0 <= ni < n and 0 <= nj < m:
                    v = m * ni + nj
                    # We pass v and get its wait time later
                    adjacent.append((v, 0))  # weight not used here
            graph[u] = adjacent
    return graph