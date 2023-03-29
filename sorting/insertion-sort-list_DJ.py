# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 하나씩 정렬된 값을 붙여나갈 예정.
        cur = parent = ListNode(None)
        
        while head:
            # cur.next가 존재 -> 하나라도 정렬된 값이 존재하는 상황.
            while cur.next and cur.next.val < head.val:
                cur = cur.next
            
            # cur.next가 False가 되어 반복문이 끝난 경우:
            # -> head.val이 현재 정렬된 모든 값보다 더 큰 경우
            # cur.next, head.next, head = head, cur.next, head.next 은
            # cur.next, head.next, head = head, None, head.next 과 같아짐.

            # cur.next.val < head.val이 False가 되어 반복문이 끝난 경우:
            # -> head.val이 현재 정렬된 연결 리스트 가운데에 들어가게 작동함.
            cur.next, head.next, head = head, cur.next, head.next

            cur = parent
        
        return cur.next