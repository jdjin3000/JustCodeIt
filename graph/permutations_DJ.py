class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        answers = []
        prev_elements = []

        def dfs(remained_elements):
            if not remained_elements:
                answers.append(prev_elements[:])
            
            for e in remained_elements:
                next_elements = remained_elements[:]
                next_elements.remove(e)
                
                prev_elements.append(e)
                dfs(next_elements)
                prev_elements.pop()
        
        dfs(nums)

        return answers

            
