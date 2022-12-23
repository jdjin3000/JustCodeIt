class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        odd = head
        even_head = even = head.next
        
        # even이 더 앞서나가 있으므로, 조건문을 even으로 걸어줌.
        while even and even.next:
            odd.next, even.next = odd.next.next, even.next.next
            odd, even = odd.next, even.next
        
        odd.next = even_head

        return head