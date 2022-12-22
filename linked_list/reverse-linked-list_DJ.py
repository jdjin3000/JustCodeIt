class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverse_nodes(prev: Optional[ListNode], remained_nodes: Optional[ListNode]) -> Optional[ListNode]:
            # 현재 위치가 None일 때, 이전 node 반환 (즉, Input linked list의 마지막 노드)
            if not remained_nodes:
                return prev
            
            # 현재 남은 linked list의 다음 node 저장. (이후 linked list에 대해 재귀적으로 수행하기 위함.)
            next_remained_nodes = remained_nodes.next
            # 현재 위치의 전 node가 현재 위치 node의 next가 되어야 하므로.
            remained_nodes.next = prev
            return reverse_nodes(remained_nodes, next_remained_nodes)

        return reverse_nodes(None, head)