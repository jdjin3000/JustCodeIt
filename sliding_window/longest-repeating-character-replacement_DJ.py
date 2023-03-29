from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest = 0

        left = 0
        countDict = defaultdict(int)

        for right, char in enumerate(s, 1):
            countDict[char] += 1

            max_key, count = max(countDict.items(), key=lambda x: x[1])

            # max 갯수를 지닌 char 말고 나머지의 합이 k 이하이면, change하여 longest 계산 가능.
            while left < right and sum(countDict.values()) - count > k:
                countDict[s[left]] -= 1
                left += 1
            
            if sum(countDict.values()) - count <= k:
                longest = max(longest, sum(countDict.values()))
        
        return longest
            