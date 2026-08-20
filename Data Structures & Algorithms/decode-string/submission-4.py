class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for char in s:
            if char == ']':
                char_str = ""
                while stack and stack[-1] != '[':
                    char_str = stack.pop() + char_str
                stack.pop()

                num = 0
                mul = 0
                while stack and stack[-1].isdigit():
                    num  += int(stack.pop()) * (10**mul)
                    mul += 1
                stack.append(num*char_str)
            else:
                stack.append(char)
        
        result = ""
        while stack:
            result = stack.pop() + result
        
        return result

            


