class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        letter = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}

        if not digits:
            return []

        answers = []
        queue = [('', list(digits))] # (current letter combination, remained digits)
        while queue:
            lt, digits = queue.pop(0)

            if not digits:
                answers.append(lt)
                continue

            for _ in letter[digits[0]]:
                queue.append((lt + _, digits[1:]))

        return answers