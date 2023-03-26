# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        p, l = head, []

        while p:
            l.append(p.val)
            p = p.next

        l.sort()

        p = head
        for i in range(len(l)):
            p.val = l[i]
            p = p.next

        return head
        