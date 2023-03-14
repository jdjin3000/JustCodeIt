class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0

        for i in range(len(s)):
            chars = []
            for char in s[i:]:
                if char in chars:
                    break
                chars.append(char)
            max_length = max(max_length, len(chars))

        return max_length