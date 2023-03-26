# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def mergeSort(l1, l2):
            if l1 is None or l2 is None:
                return l1 or l2 # 둘 중 하나가 None이면, None이 아닌 것이 return. 둘 다 None이 아니면, 먼저 것 (l1)이 return.
            
            head = pointer = ListNode()

            while l1 and l2:
                if l1.val < l2.val:
                    pointer.next, l1 = l1, l1.next
                else:
                    pointer.next, l2 = l2, l2.next
                
                pointer = pointer.next

            pointer.next = l1 or l2

            return head.next


        if head is None or head.next is None:
            return head

        slow = fast = head

        while fast and fast.next:
            half, slow, fast = slow, slow.next, fast.next.next

        half.next = None # linked list를 두개로 나눔

        l1 = self.sortList(head)
        l2 = self.sortList(slow)

        return mergeSort(l1, l2)
                

        
    
