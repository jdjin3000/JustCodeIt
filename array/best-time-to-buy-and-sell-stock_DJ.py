class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = max(prices)
        profit = 0

        for b_p in prices:
            min_price = min(b_p, min_price)
            profit = max(profit, b_p - min_price)

        return profit