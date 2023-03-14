class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        answer = 0
        
        for stone in stones:
            answer += 1 if stone in jewels else 0

        return answer