from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = Counter()
        result = []
        for n in nums:
            cnt[n] += 1
        
        top = cnt.most_common()

        for i in range(k):
            result.append(top[i][0])

        return result