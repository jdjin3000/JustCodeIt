from collections import defaultdict

class ListNode:
    def __init__(self, key=None, val=None, next=None):
        self.key = key
        self.val = val
        self.next = None

class MyHashMap:
    def __init__(self):
        self.hashmap = defaultdict(ListNode)
        self.hash_fn = lambda key: key % 1000 # 임의의 hash function

    def put(self, key: int, value: int) -> None:
        if self.hashmap[self.hash_fn(key)].key is None:
            self.hashmap[self.hash_fn(key)] = ListNode(key, value)
        else:
            head = self.hashmap[self.hash_fn(key)]
            while head:
                if head.key == key:
                    head.val = value
                    return
                if head.next is None:
                    break

                head = head.next
            
            head.next = ListNode(key, value)

    def get(self, key: int) -> int:
        head = self.hashmap[self.hash_fn(key)]

        while head:
            if head.key == key:
                return head.val
            head = head.next
        
        return -1

    def remove(self, key: int) -> None:
        prev = head = self.hashmap[self.hash_fn(key)]

        if head.key is None:
            return

        if head.key == key:
            self.hashmap[self.hash_fn(key)] = ListNode() if head.next is None else head.next
            return

        while head:
            if head.key == key:
                prev.next = head.next
                break
            
            prev, head = head, head.next

        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)