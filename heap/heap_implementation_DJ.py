
class BinaryHeap:
    def __init__(self):
        self.heap = [None] # index 1부터 시작하기 위해서
    
    def __len__(self):
        return len(self.heap) - 1
    
    def _percolate_up(self):
        idx = len(self)
        parent_idx = idx // 2

        while parent_idx > 0:
            if self.heap[idx] < self.heap[parent_idx]: # min_heap
                self.heap[idx], self.heap[parent_idx] = self.heap[parent_idx], self.heap[idx]
            idx = parent_idx
            parent_idx = idx // 2

    def insert(self, item):
        self.heap.append(item)
        self._percolate_up()

    def _percolate_down(self):
        idx = 1
        
        while idx < len(self.heap):
            left, right = idx * 2, idx * 2 + 1

            if left < len(self.heap) and self.heap[left] < self.heap[idx]:
                self.heap[left], self.heap[idx] = self.heap[idx], self.heap[left]
                idx = left
            elif right < len(self.heap) and self.heap[right] < self.heap[idx]:
                idx = right
            else:
                break
        

    def extract(self):
        popped, self.heap[1] = self.heap[1], self.heap.pop()
        self._percolate_down()

        return popped
    

# a = BinaryHeap()

# a.insert(4)
# a.insert(2)
# a.insert(3)
# a.insert(1)

# print(a.heap)

# print(f"popped: {a.extract()}")
# print(a.heap)

# print(f"popped: {a.extract()}")
# print(a.heap)

# a.insert(1)
# print(a.heap)

# a.insert(2)
# print(a.heap)

# print(f"popped: {a.extract()}")
# print(a.heap)

# print(f"popped: {a.extract()}")
# print(a.heap)
