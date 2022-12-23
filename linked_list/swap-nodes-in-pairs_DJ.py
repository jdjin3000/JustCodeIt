class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head and head.next:
            # p is B.
            p = head.next
            # A's next has changed.
            head.next = self.swapPairs(p.next) # p.next is B's next (=C). It means function considers swap pairs, recursively.
            # p (=B)'s next has changed to head (=A).
            p.next = head
            return p
        return head