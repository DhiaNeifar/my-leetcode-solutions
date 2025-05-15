class MyQueue:

    def __init__(self):
        self.stack_1 = []
        self.stack_2 = []

    def push(self, x: int) -> None:
        self.stack_1.append(x)

    def pop(self) -> int:
        while self.stack_1:
                x = self.stack_1.pop()
                self.stack_2.append(x)
        a = self.stack_2.pop()
        while self.stack_2:
            x = self.stack_2.pop()
            self.stack_1.append(x)
        return a

    def peek(self) -> int:
        if self.stack_1:
            return self.stack_1[0]

    def empty(self) -> bool:
        if self.stack_1:
            return False
        return True


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()