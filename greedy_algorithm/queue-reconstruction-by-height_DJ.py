'''
list().insert(index, value): index 위치에 value를 넣음.

위 함수가 핵심. Greedy하게 같은 k_i를 가진 값들 중 작은 h_i를 가진 것을 상대적으로 앞에 넣어야 모순이 생기지 않음.
'''

from heapq import heappush, heappop

class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        heap, answer = [], []
        
        for h_i, k_i in people:
            heappush(heap, (-h_i, k_i))
        
        for _ in range(len(heap)):
            h_i, k_i = heappop(heap)
            answer.insert(k_i, (-h_i, k_i))
        
        return answer