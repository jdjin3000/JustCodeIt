from collections import Counter

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        answer = {v: k for k, v in Counter(nums).items()}

        return answer[1]