from collections import deque
from typing import List, Tuple

class Solution:
    def minMoves(self, classroom: List[str], energy: int) -> int:
        m, n = len(classroom), len(classroom[0])
        lumetarkon = classroom

        litter_pos = []
        litter_id_map = {}
        start = None

        for i in range(m):
            for j in range(n):
                if classroom[i][j] == 'S':
                    start = (i, j)
                elif classroom[i][j] == 'L':
                    litter_id = len(litter_pos)
                    litter_pos.append((i, j))
                    litter_id_map[(i, j)] = litter_id

        full_mask = (1 << len(litter_pos)) - 1

        queue = deque()
        visited = dict()

        queue.append((start[0], start[1], full_mask, energy, 0))
        visited[(start[0], start[1], full_mask)] = energy

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        while queue:
            row, col, mask, curr_energy, moves = queue.popleft()

            if mask == 0:
                return moves

            if curr_energy == 0 and classroom[row][col] != 'R':
                continue

            if classroom[row][col] == 'R':
                curr_energy = energy

            for dr, dc in directions:
                nr, nc = row + dr, col + dc
                if 0 <= nr < m and 0 <= nc < n and classroom[nr][nc] != 'X':
                    new_mask = mask
                    if (nr, nc) in litter_id_map and (mask & (1 << litter_id_map[(nr, nc)])):
                        new_mask = mask & ~(1 << litter_id_map[(nr, nc)])
                    new_energy = curr_energy - 1
                    state_key = (nr, nc, new_mask)
                    if state_key not in visited or visited[state_key] < new_energy:
                        visited[state_key] = new_energy
                        queue.append((nr, nc, new_mask, new_energy, moves + 1))

        return -1