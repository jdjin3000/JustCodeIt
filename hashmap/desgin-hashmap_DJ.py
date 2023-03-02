class ListNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class MyHashMap:
    def __init__(self):
        self.size = 1000
        self.hashmap = [None] * self.size
        self.hash_fn = lambda x: x % self.size

    def put(self, key: int, value: int) -> None:
        hash_key = self.hash_fn(key)

        if self.hashmap[hash_key] is None:
            self.hashmap[hash_key] = ListNode(key, value)
            return

        cur_node = self.hashmap[hash_key]
        while cur_node is not None:
            if cur_node.key == key:
                cur_node.value = value
                break
            elif cur_node.next is None:
                cur_node.next = ListNode(key, value)
                break
            
            cur_node = cur_node.next

    def get(self, key: int) -> int:
        hash_key = self.hash_fn(key)

        cur_node = self.hashmap[hash_key]
        while cur_node is not None:
            if cur_node.key == key:
                return cur_node.value
            else:
                cur_node = cur_node.next
        
        return -1

    def remove(self, key: int) -> None:
        hash_key = self.hash_fn(key)
        
        cur_node = self.hashmap[hash_key]

        if cur_node is None:
            return

        if cur_node.key == key:
            self.hashmap[hash_key] = cur_node.next
            return
        
        prev_node = cur_node
        cur_node = cur_node.next
        while cur_node is not None:
            if cur_node.key == key:
                prev_node.next = cur_node.next
                break

            prev_node = cur_node
            cur_node = cur_node.next