class Solution:
    def isPalindrome(self, s: str) -> bool:
        alphanumeric = "abcdefghijklmnopqrstuvwxyz0123456789"
        lower_s = "".join([_ for _ in s.lower() if _ in alphanumeric])
        reversed_s = "".join([_ for _ in lower_s[::-1]])

        if lower_s[:len(lower_s)//2] == reversed_s[:len(lower_s)//2]:
            return True
        else:
            return False