from collections import deque

class MyQueue:
    def __init__(self):
        self.stack = deque()
        self.sub_stack = deque()

    def push(self, x: int) -> None:
        # deque().append(): "push to top"
        self.stack.append(x)

    def pop(self) -> int:
        # deque().pop(): "peek/pop from top"
        while len(self.stack) > 1:
            self.sub_stack.append(self.stack.pop())
        
        popped = self.stack.pop()
        while len(self.sub_stack):
            self.stack.append(self.sub_stack.pop())

        return popped

    def peek(self) -> int:
        while len(self.stack) > 1:
            self.sub_stack.append(self.stack.pop())
        
        popped = self.stack.pop()
        self.stack.append(popped)
        while len(self.sub_stack):
            self.stack.append(self.sub_stack.pop())

        return popped

    def empty(self) -> bool:
        return False if len(self.stack) else True