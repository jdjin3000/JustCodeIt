class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        answer = ListNode()
        pointer = answer
        carry = 0
        # 한 linked list가 먼저 끝에 도달하는 경우, 모든 linked list 사용 후 carry가 남았을 경우 고려
        while l1 or l2 or carry:
            digit_sum = 0
            digit_sum += l1.val if l1 else 0
            digit_sum += l2.val if l2 else 0
            
            carry, remainder = (digit_sum + carry) // 10, (digit_sum + carry) % 10
            pointer.next = ListNode(remainder)
            pointer = pointer.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        # 첫 node는 val을 update하지 않았으므로 제외.
        return answer.next