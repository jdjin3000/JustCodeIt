class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest = prices[0]
        profit = 0

        for price in prices:
            # 가장 작은 값을 갱신
            if price < lowest:
                lowest = price
            
            # 현재 값과의 차이가 최대가 될 때를 profit에 저장
            if profit < (price - lowest):
                profit = price - lowest
        return profit