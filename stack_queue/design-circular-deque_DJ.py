class MyCircularDeque:

    def __init__(self, k: int):
        self.deque = [None for _ in range(k)]
        self.front = 0
        self.rear = 0

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False

        self.deque[self.front - 1] = value
        self.front = (self.front - 1) % len(self.deque)

        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
    
        self.deque[self.rear] = value
        self.rear = (self.rear + 1) % len(self.deque)

        return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        
        self.deque[self.front] = None
        self.front = (self.front + 1) % len(self.deque)

        return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        
        self.deque[self.rear - 1] = None
        self.rear = (self.rear - 1) % len(self.deque)

        return True

    def getFront(self) -> int:
        return self.deque[self.front] if not self.isEmpty() else -1

    def getRear(self) -> int:
        return self.deque[self.rear - 1] if not self.isEmpty() else -1
        
    def isEmpty(self) -> bool:
        return True if self.front == self.rear and self.deque[0] == None else False

    def isFull(self) -> bool:
        return True if self.front == self.rear and self.deque[0] != None else False