class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # Case 1) sum(gas) < sum(cost): 가능한 출발점이 존재하지 않는다.
        if sum(gas) < sum(cost):
            return -1
        
        # Case 2) sum(gas) >= sum(cost)
        # 문제 제약 상, 단 하나의 출발점만이 존재한다.
        # 한 번씩 순회하면서 해당 지점이 출발점으로 적합한지 계산한다.
        # 임의의 시점의 Gas와 Cost만 고려하여 출발점이 가능한지 고려한다.
        # i) 가능하다면 계속 쌓아 나가며 계산해나간다.
        # ii) 불가능하다면 지나온 이전 모든 station은 시작점으로서 부적합하므로, 다음 station부터 시작점으로 고려한다.
        # why) 통과했을 경우 각 station마다 남는 gas는 0 이상인데, 넘어가기 불가능한 지점을 발견하면 시작점과 불가능한 지점 가운데에서 start하면 더더욱 gas가 적을 것이므로.

        start_idx, remained_gas = 0, 0
        for i, station_gas in enumerate(gas):
            if remained_gas + station_gas < cost[i]:
                start_idx = i + 1
                remained_gas = 0
            else:
                remained_gas += station_gas - cost[i]

        return start_idx