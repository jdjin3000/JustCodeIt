class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # 현재 노드의 값이 상대적으로 작은 것을 l1으로 지정함.
        # not list1은 None일 경우를 고려한 조건문임. 한 linked list만 None이면 or 조건에 의해 실행 됨.
        if (not list1) or (list2 and list1.val > list2.val):
            list1, list2 = list2, list1
        
        # 작은 node 확정, 그 이후 (list1.next)를 정하기 위해 현재 확정된 노드를 제외한 linked list (list1.next, list2)들을 사용해 재귀.
        if list1:
            list1.next = self.mergeTwoLists(list1.next, list2)
        
        return list1