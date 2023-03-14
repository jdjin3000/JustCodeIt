class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left_window = max_length = 0
        seen = dict()

        for i, char in enumerate(s):
            # left_window > seen[char]면 seen에 해당되어도 window 안에는 포함이 안되므로 괜찮음.
            if char in seen and left_window <= seen[char]:
                left_window = seen[char] + 1
            else:
                # i가 right window 역할을 함. (sliding window)
                max_length = max(max_length, i - left_window + 1)

            seen[char] = i

        return max_length