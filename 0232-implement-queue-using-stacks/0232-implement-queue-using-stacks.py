class MyQueue:

    def __init__(self):
        self.stack = [] 
        self.output = [] 

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> int:
        self.peek()
        p = self.output.pop()
        return p 

    def peek(self) -> int:
        if not self.output:
            while self.stack:
                self.output.append(self.stack.pop())

        return self.output[-1]

    def empty(self) -> bool:
        return not self.stack and not self.output


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()