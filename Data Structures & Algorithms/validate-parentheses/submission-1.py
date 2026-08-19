class Solution:
    def isValid(self, s: str) -> bool:
        bracket_stack = []
        for char in s:
            if char == '}':
                if bracket_stack and bracket_stack[-1] == '{':
                    bracket_stack.pop()
                else:
                    return False
            elif char == ')':
                if bracket_stack and bracket_stack[-1] == '(':
                    bracket_stack.pop()
                else:
                    return False
            elif char == ']':
                if bracket_stack and bracket_stack[-1] == '[':
                    bracket_stack.pop()
                else:
                    return False
            else:
                bracket_stack.append(char)
        
        if len(bracket_stack) == 0:
            return True
        return False