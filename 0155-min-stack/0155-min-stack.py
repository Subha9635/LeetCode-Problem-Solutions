class MinStack:

    def __init__(self):
        self.stack = []
        self.mini = float('inf')

    def push(self, value: int) -> None:
        if not self.stack:
            self.stack.append(value)
            self.mini = value
        else:
            if value <= self.mini:
                self.stack.append(2*value-self.mini)
                self.mini = value
            else:
                self.stack.append(value)

    def pop(self) -> None:
        if self.stack:
            x = self.stack[-1]
            self.stack.pop()
            if x < self.mini:
                self.mini = (2*self.mini-x)

    def top(self) -> int:
        if self.stack:
            if self.stack[-1] < self.mini:
                return self.mini
            return self.stack[-1]

    def getMin(self) -> int:
        return self.mini


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()