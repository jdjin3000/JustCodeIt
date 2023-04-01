class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        def compute(left, char, right):
            result = []

            for l in left:
                for r in right:
                    result.append(eval(str(l) + char + str(r)))

            return result

        if expression.isdigit():
            return [int(expression)]
        
        answer = []
        for idx, char in enumerate(expression):
            if char in '+-*':
                left = self.diffWaysToCompute(expression[:idx])
                right = self.diffWaysToCompute(expression[idx + 1:])

                answer.extend(compute(left, char, right))

        return list(map(int, answer))
                