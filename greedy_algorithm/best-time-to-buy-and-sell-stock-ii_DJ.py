'''
전형적인 Greedy Algorithm 문제.
사고 파는 것에 제한이 없으므로, 상승하기 전에 사고 하락하기 전에 팔면 됨.

주가 Chart를 그렸을 때, 기울기가 양인 모든 경우를 더한다고 보면 이해 쉬울 듯.
'''

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        answer = 0

        for i, buy_p in enumerate(prices[:-1]):
            if prices[i + 1] - buy_p > 0:
                answer += prices[i + 1] - buy_p

        return answer
            