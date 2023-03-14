# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from heapq import heappush, heappop

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        answers = head = ListNode(None)
        heap = []
        
        for i, list_ in enumerate(lists):
            if list_:
                # index는 필요없지만 heap에 동일한 값이 들어가 오류가 발생하는 것을 막기 위한 조치임.
                heappush(heap, (list_.val, i, list_))

        while heap:
            val, i, list_ = heappop(heap)
            
            head.next, list_ = list_, list_.next
            head = head.next

            if list_:
                heappush(heap, (list_.val, i, list_))
        
        return answers.next