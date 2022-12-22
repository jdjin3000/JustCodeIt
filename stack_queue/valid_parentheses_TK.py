class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for p in s:
            if len(stack) == 0:
                stack.append(p)
            elif stack[-1] == '(' and p ==')':
                stack.pop()
            elif stack[-1] == '{' and p == '}':
                stack.pop()
            elif stack[-1] == '[' and p == ']':
                stack.pop()
            else:
                stack.append(p)

        
        if not stack:
            return True
        else:
            return False