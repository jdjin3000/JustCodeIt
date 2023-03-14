from collections import defaultdict

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)
        tickets.sort()

        for departure, arrival in tickets:
            graph[departure].append(arrival)
        
        answer = []

        def dfs(departure):
            # graph[departure]가 False일 케이스
            # 1. 전체 여정의 마지막 종착지인 경우. (모든 티켓을 씀)
            # 2. 중간에 잘못된 방향을 선택해서 티켓을 다 쓰지 않은채로 갈 곳이 없는 경우.
            
            # 둘 다 하나의 Logic으로 해결이 가능하다.
            # 만약 'A'라는 도착지를 맨 처음 선택해 dfs('A')가 호출되었다고 가정하자.
            # 만약 2번의 경우에 해당되었을 경우, 전체 여정에서 'A'는 마지막 여행지에 해당이 되었을 것이다.
            # 문제 조건 상, 모든 티켓은 한번씩 무조건 사용해야 하기 때문이다. (You must use all the tickets once and only once.)
            while graph[departure]:
                dfs(graph[departure].pop(0))
            answer.append(departure)

        dfs("JFK")

        return answer[::-1]