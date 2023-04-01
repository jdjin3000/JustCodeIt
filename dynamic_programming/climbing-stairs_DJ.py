from collections import defaultdict

class Solution:
    def __init__(self):
        # n개의 계단을 오르는 방법의 수를 F(n)이라고 하면, 
        # 계단을 오르는 마지막 단계에서 가능한 경우의 수는 
        # 마지막 계단에서 1개의 단계를 올라가는 경우와 마지막 계단에서 2개의 단계를 올라가는 경우입니다.
        self.dp = defaultdict(int)

    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n

        if self.dp[n]:
            return self.dp[n]
        
        self.dp[n] = self.climbStairs(n - 1) + self.climbStairs(n - 2)
        return self.dp[n]