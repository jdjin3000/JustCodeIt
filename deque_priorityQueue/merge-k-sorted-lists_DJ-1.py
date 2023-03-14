# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        answers = head = ListNode(None)

        # 예외 처리
        while None in lists:
            lists.remove(None)

        while lists:
            lists.sort(key=lambda x: x.val)

            head.next, lists[0] = lists[0], lists[0].next
            head = head.next

            if None in lists:
                lists.remove(None)

        return answers.next