from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()

        for _ in s:
            if _ in ['(', '{', '[']:
                stack.append(_)
            # preventing 'pop from an empty deque'
            elif not len(stack):
                return False
            else:
                bracket = stack.pop()
                if not ''.join([bracket, _]) in ['()', '{}', '[]']:
                    stack.extend([bracket, _])
        
        return True if not len(stack) else False