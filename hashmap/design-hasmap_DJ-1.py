from collections import defaultdict

class MyHashMap:
    def __init__(self):
        self.hashmap = defaultdict(None)

    def put(self, key: int, value: int) -> None:
        self.hashmap[key] = value

    def get(self, key: int) -> int:
        return -1 if key not in self.hashmap or self.hashmap[key] is None else self.hashmap[key]

    def remove(self, key: int) -> None:
        if key in self.hashmap:
            self.hashmap.pop(key)
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)