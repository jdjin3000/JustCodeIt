class MyCircularQueue:
    def __init__(self, k: int):
        self.circular_queue = [None for _ in range(k)]
        self.front = 0
        self.rear = 0

    def enQueue(self, value: int) -> bool:
        # None과의 비교를 반드시 명시해 줘야 함. 그렇지 않으면 value == 0 일 때 오작동.
        if self.circular_queue[self.rear] != None:
            return False

        self.circular_queue[self.rear] = value
        self.rear = (self.rear + 1) % len(self.circular_queue)

        return True
        

    def deQueue(self) -> bool:
        if self.circular_queue[self.front] == None:
            return False

        self.circular_queue[self.front] = None
        self.front = (self.front + 1) % len(self.circular_queue)

        return True
        

    def Front(self) -> int:
        if self.isEmpty():
            return -1

        return self.circular_queue[self.front]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1

        return self.circular_queue[self.rear - 1]

    def isEmpty(self) -> bool:
        return True if self.front == self.rear and self.circular_queue[0] == None else False
    
    def isFull(self) -> bool:
        return True if self.front == self.rear and self.circular_queue[0] != None else False
