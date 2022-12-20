# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head
        prev = None

        while node is not None:
            # prev, node - 이전노드와 현재노드를 가리키는 포인터 역할
            # tmp = 다음 노드로 이동시키기 위한 값 
            tmp = node.next
            node.next = prev 
            prev = node 
            node = tmp 
                
        return prev