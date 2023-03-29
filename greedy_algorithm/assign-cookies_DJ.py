class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()

        answer = 0

        while g and s:
            if g[0] > s[0]:
                s.pop(0)
            else: # Satisfying
                g.pop(0)
                s.pop(0)
                answer += 1
        
        return answer