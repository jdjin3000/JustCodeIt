from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = Counter(t)
        set_t = set(t)
        left, start, end = 0, 0, 0


        for right, char in enumerate(s, 1): # right 1번부터 시작
            need[char] -= 1

            if all([need[_] <= 0 for _ in set_t]): # 조건을 만족할 때: s such that every character in t (including duplicates) is included in the window
                while left < right and need[s[left]] < 0:
                    need[s[left]] += 1
                    left += 1
                
                # not end: end가 0일 때
                # right - left <= end - start: 현재 발견한 답이 기존 답보다 짧을 때
                if not end or right - left <= end - start:
                    start, end = left, right
                    need[s[left]] += 1
                    left += 1

        return s[start:end]