from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        sorted_nums = sorted(Counter(nums).items(), key=lambda x: x[1], reverse=True)

        return [element for element, num in sorted_nums[:k]]