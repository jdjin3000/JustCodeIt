class Solution:
    def longestPalindrome(self, s: str) -> str:
        def findPalindrome(s: str, left: int, right: int) -> bool:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left+1:right]
        
        if len(s) < 2:
            return s

        answer = ""

        for i in range(len(s)-1):
            answer = max([answer, findPalindrome(s, i, i+1), findPalindrome(s, i, i+2)], key=len)
        
        return answer