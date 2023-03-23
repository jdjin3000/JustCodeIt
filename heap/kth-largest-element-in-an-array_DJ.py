from heapq import heappush, heappop
from collections import Counter
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []

        for num, i in Counter(nums).items():
            heappush(heap, (-num, i))

        for _ in range(k):
            num, i = heappop(heap)
            if i - 1 > 0: # 하나씩 차감
                heappush(heap, (num, i - 1))

        return -num