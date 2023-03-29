from collections import defaultdict, Counter, deque

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
    
        init_s_len, min_substring = len(s), "#" * (len(s) + 1)

        t_count, t_set = defaultdict(int, Counter(t)), set(t)
        window, s = deque(s[:len(t)]), deque(s[len(t):]) # 가장 최소의 window size

        # 초기 세팅
        for char in window:
            t_count[char] -= 1

        while s or all([t_count[char] <= 0 for char in t_set]):
            if not window:
                break

            if all([t_count[char] <= 0 for char in t_set]): # window 내에서 모든 t 문자를 포함할 때
                while all([t_count[char] <= 0 for char in t_set]):
                    removed = window.popleft()
                    t_count[removed] += 1

                # while 조건문 내에서 마지막으로 popleft된 것을 포함해야 all([t_count[char] <= 0 for char in t_set])를 만족하는 가장 짧은 문자열이 되므로.
                window.appendleft(removed)
                t_count[removed] -= 1
                min_substring = min(min_substring, "".join(window), key=len)

                removed = window.popleft()
                t_count[removed] += 1
            else:
                added = s.popleft()
                window.append(added)
                t_count[added] -= 1

        return "" if len(min_substring) > init_s_len else min_substring