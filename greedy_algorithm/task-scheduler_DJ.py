from heapq import heappush, heappop
from collections import Counter

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        answer = []

        # 우선 가장 많은 task 부터 시작하는 것이 최적. 미리 해놓아야 최대한 idle 없이 진행할 수 있으므로.
        tasks_heap, deactivated = [], []
        for k, v in Counter(tasks).items():
            heappush(tasks_heap, (-v, k)) # 최대 힙으로 만들기 위해.

        time = -1
        while tasks_heap or deactivated:
            time += 1
            while deactivated and time - deactivated[0][1] > n: # 같은 task 사이에 n 만큼의 여유가 있어야 하므로.
                activated, _ = deactivated.pop(0)
                heappush(tasks_heap, activated)

            if tasks_heap:
                remained, task = heappop(tasks_heap)
                answer.append(task)

                if remained + 1 != 0: # 남은 task 횟수가 있을 때
                    deactivated.append(((remained + 1, task), time)) # 초기화 할 때, 남은 횟수에 -1을 곱했으므로 +1로 횟수 감량.
            else:
                answer.append('idle')

        return len(answer)