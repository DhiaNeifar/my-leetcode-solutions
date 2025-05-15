class Solution:
    def specialGrid(self, N: int) -> List[List[int]]:
        if N == 0:
            return [[0]]
        def fill_grid(x_start, x_finish, y_start, y_finish):
            nonlocal val
            if x_start + 1 == x_finish and y_start + 1 == y_finish:
                grid[x_start - 1][y_finish - 1] = val[0]
                val[0] += 1
                grid[x_finish - 1][y_finish - 1] = val[0]
                val[0] += 1
                grid[x_finish - 1][y_start - 1] = val[0]
                val[0] += 1
                grid[x_start - 1][y_start - 1] = val[0]
                val[0] += 1
                return
    
    
            x_half = (x_finish + x_start) // 2
            y_half = (y_finish + y_start) // 2
    
            # Upper Right Quadrant
            fill_grid(x_start, x_half, y_half + 1, y_finish)
    
            # Lower Right Quadrant
            fill_grid(x_half + 1, x_finish, y_half + 1, y_finish)
    
            # Lower Left Quadrant
            fill_grid(x_half + 1, x_finish, y_start, y_half)
    
            # Upper Left Quadrant
            fill_grid(x_start, x_half, y_start, y_half)
    
        val = [0]
        grid_size = 2 ** N
        grid = [[0 for _ in range(grid_size)] for _ in range(grid_size)]
        fill_grid(1, grid_size, 1, grid_size)
        return grid