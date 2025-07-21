class MovingAverage:

    def __init__(self, size: int):
        self.size = size
        self.actual_size = 0
        self.stack = [0 for _ in range(self.size)]
        self.curr_index = 0
        
    def next(self, val: int) -> float:
        self.stack[self.curr_index] = val
        self.curr_index += 1
        self.curr_index %= self.size
        self.actual_size = min(self.size, self.actual_size + 1)
        return sum(self.stack) / self.actual_size


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)