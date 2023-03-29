class Solution:
    def isPalindrome(self, s: str) -> bool:
        alphabet = "abcdefghijklmnopqrstuvwxyz0123456789"
        s = [c.lower() for c in s if c.lower() in alphabet]

        return s == s[::-1]