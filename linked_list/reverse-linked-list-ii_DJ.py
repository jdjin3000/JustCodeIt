class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        root = start = ListNode(None)
        root.next = head

        # reverse 시작을 위한 start node 찾기
        for _ in range(left - 1):
            start = start.next
        end = start.next
        
        # 구간 내의 노드 개수 만큼 시도
        for _ in range(right - left):
            tmp, start.next, end.next = start.next, end.next, end.next.next
            start.next.next = tmp
        return root.next