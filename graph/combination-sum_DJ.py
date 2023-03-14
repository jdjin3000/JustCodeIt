class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        answers = set()

        def dfs(elements):
            if sum(elements) == target:
                answers.add(tuple(sorted(elements[:])))
                return
            
            if sum(elements) > target:
                return

            for e in candidates:
                elements.append(e)
                dfs(elements)
                elements.pop()
            
        dfs([])

        return list(map(list, answers))