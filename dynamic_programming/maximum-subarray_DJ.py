# Kadane's algorithm

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        answer = float('-inf')
        
        current_sum = 0
        for num in nums:
            current_sum = max(current_sum + num, num)
            answer = max(answer, current_sum)

        return answer