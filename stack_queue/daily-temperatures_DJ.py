class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = list()
        answer = [0 for _ in range(len(temperatures))]
        
        for i, t_ in enumerate(temperatures):
            while stack and stack[-1][1] < t_:
                top_i, top_temp = stack.pop()
                answer[top_i] = i - top_i
            
            stack.append((i, t_))

        return answer