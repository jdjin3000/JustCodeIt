# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        lst = []

        # head가 비어있는 경우
        if head is None:
            return False

        node = head

        while node is not None:
            lst.append(node.val)
            node = node.next
        
        if lst == lst[::-1]:
            return True
        else:
            return False