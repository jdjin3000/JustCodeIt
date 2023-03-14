class MyCircularDeque:

    def __init__(self, k: int):
        self.k = k
        self.queue = [None] * k
        self.front, self.rear = 0, 0

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False

        self.front = (self.front - 1) % self.k
        self.queue[self.front] = value

        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False

        self.queue[self.rear] = value
        self.rear = (self.rear + 1) % self.k

        return True
        

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False

        self.queue[self.front] = None
        self.front = (self.front + 1) % self.k

        return True
        

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False

        self.rear = (self.rear - 1) % self.k
        self.queue[self.rear] = None

        return True

    def getFront(self) -> int:
        if self.isEmpty():
            return -1
        
        return self.queue[self.front]

    def getRear(self) -> int:
        if self.isEmpty():
            return -1
        
        return self.queue[(self.rear - 1) % self.k]

    def isEmpty(self) -> bool:
        return self.front == self.rear and self.queue[self.front] == None

    def isFull(self) -> bool:
        return self.front == self.rear and self.queue[self.front] != None