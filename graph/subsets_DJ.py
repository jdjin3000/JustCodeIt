class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        answers = []
        prev_elements = []

        def dfs(remained_elements):
            if not prev_elements in answers:
                answers.append(prev_elements[:])

            for i, e in enumerate(remained_elements):
                prev_elements.append(e)
                dfs(remained_elements[i+1:])
                prev_elements.pop()
            
        dfs(nums)

        return answers
            