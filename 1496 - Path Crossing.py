class Solution:
    def isPathCrossing(self, path: str) -> bool:
        curr_pos = [0, 0]
        all_points = [[0, 0]]
        for direction in path:
            if direction == 'N':
                curr_pos[1] += 1
            if direction == 'S':
                curr_pos[1] -= 1
            if direction == 'E':
                curr_pos[0] += 1
            if direction == 'W':
                curr_pos[0] -= 1
            if curr_pos in all_points:
                return True
            all_points.append([curr_pos[0], curr_pos[1]])
        return False