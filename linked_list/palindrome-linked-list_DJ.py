class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        text = ""
        
        while head:
            text += str(head.val)
            head = head.next

        if len(text) % 2 == 0 and text[:len(text)//2] == text[-1:len(text)//2-1:-1]:
            return True
        elif len(text) % 2 == 1 and text[:len(text)//2] == text[-1:len(text)//2:-1]:
            return True
        return False