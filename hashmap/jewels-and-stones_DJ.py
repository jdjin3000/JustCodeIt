from collections import defaultdict

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        hashmap = defaultdict(int)

        for stone in stones:
            hashmap[stone] += 1
        
        return sum([hashmap[jewel] for jewel in jewels])