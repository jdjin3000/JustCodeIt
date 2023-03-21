from collections import defaultdict

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]

        edges_list = defaultdict(list)

        for i, j in edges:
            edges_list[i].append(j)
            edges_list[j].append(i)

        # 둘 중 하나가 leaf node가 될 수 밖에 없는 edge를 찾아서 없애 나가면,
        # 가장 많은 node와 연결된 node만이 남을 것이고, 해당 node가 root일 때 가장 높이가 낮을 것.
        
        # node: 1, 2, ..., n
        leaf_nodes = [i for i in range(n+1) if len(edges_list[i]) == 1]

        remained_nodes = n
        while remained_nodes > 2: # edge는 양방향이니까 nodes == 2일 때 작동하면 안 됨. 작동하면 마지막 edge도 사라짐.
            new_leaf_nodes = []
            for i in leaf_nodes:
                neighbor = edges_list[i].pop()
                edges_list[neighbor].remove(i)

                # for문이 끝나고 처리하면 안 됨. 예시) n = 4, edges = [[1,0],[1,2],[1,3]]
                if len(edges_list[neighbor]) == 1:
                    new_leaf_nodes.append(neighbor)
            
            remained_nodes -= len(leaf_nodes)
            leaf_nodes = new_leaf_nodes
        
        return leaf_nodes

