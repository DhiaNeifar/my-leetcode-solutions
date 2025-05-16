class MyStack:

    def __init__(self):
        self.queue1 = []
        self.queue2 = [] 

    def push(self, x: int) -> None:
        self.queue1.append(x)

    def pop(self) -> int:
        element = self.queue1.pop(0)
        while not self.empty():
            self.queue2.append(element)
            element = self.queue1.pop(0)
        self.queue1, self.queue2 = self.queue2, self.queue1
        return element
        

    def top(self) -> int:
        if not self.empty():
            return self.queue1[-1]

    def empty(self) -> bool:
        return len(self.queue1) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()