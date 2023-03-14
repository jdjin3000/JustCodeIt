class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        answers = []
        prev_elements = []
        
        def dfs(remained_elements):
            if len(prev_elements) == k:
                answers.append(prev_elements[:])
                return
            
            for i, e in enumerate(remained_elements):
                next_elements = remained_elements[i+1:]

                prev_elements.append(e)
                dfs(next_elements)
                prev_elements.pop()

        dfs(list(range(1, n + 1)))

        return answers