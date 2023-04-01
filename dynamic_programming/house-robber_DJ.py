class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        dp = [None for _ in nums]
        dp[-1], dp[-2] = nums[-1], max(nums[-1], nums[-2]) # 판단을 통해 해당 idx 이후로 얻을 수 있는 최대 값.

        def houseRobber(idx: int):
            if idx >= len(nums):
                return 0

            if dp[idx] is not None:
                return dp[idx]
        
            dp[idx] = max(nums[idx] + houseRobber(idx + 2), houseRobber(idx + 1))

            return dp[idx]

        return houseRobber(0)