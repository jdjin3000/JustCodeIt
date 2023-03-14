from collections import defaultdict
from heapq import heappop, heappush

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        delay = {i+1: float('inf') for i in range(n)}
        delay[k] = 0

        graph = defaultdict(list)
        for i, j, weight in times:
            graph[i].append((j, weight)) # (target, weight)

        heap = []
        
        def dijkstra(start):
            heappush(heap, (0, start)) # (distance from start to '~', '~')

            while heap:
                distance, current_state = heappop(heap)

                for target, weight in graph[current_state]:
                    if distance + weight < delay[target]:
                        delay[target] = distance + weight
                        heappush(heap, (distance + weight, target))

        dijkstra(k)
        delay.pop(k) # 자기 자신이므로 제외

        # 가장 오래 걸린 것이 마지막 남은 전파 대상자일테므로 max
        return -1 if float('inf') in delay.values() else max(delay.values())