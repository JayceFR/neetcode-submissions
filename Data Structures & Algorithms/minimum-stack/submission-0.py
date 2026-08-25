class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

    def pop(self) -> None:
        if self.stack:
            self.stack.pop(len(self.stack)-1)

    def top(self) -> int:
        if self.stack:
            return self.stack[len(self.stack)-1]

    def getMin(self) -> int:
        return min(self.stack)
