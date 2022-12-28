from collections import deque

class MyStack:
    def __init__(self):
        self.queue = deque()
        self.sub_queue = deque()

    def push(self, x: int) -> None:
        # deque().append(): "push to back"
        self.queue.append(x) 

    def pop(self) -> int: 
        # Below code could be simplified by using deque().rotate(), but I focused on using queue's standard operations.
        # deque().popleft(): "peek/pop from front"
        while len(self.queue) > 1:
            self.sub_queue.append(self.queue.popleft())
        
        while len(self.sub_queue):
            self.queue.append(self.sub_queue.popleft())

        return self.queue.popleft()

    def top(self) -> int:
        while len(self.queue) > 1:
            self.sub_queue.append(self.queue.popleft())
        
        topped = self.queue.popleft()
        
        while len(self.sub_queue):
            self.queue.append(self.sub_queue.popleft())
        self.queue.append(topped)

        return topped

    def empty(self) -> bool:
        return False if len(self.queue) else True