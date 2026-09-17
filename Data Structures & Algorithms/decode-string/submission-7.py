class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        num = 0
        string = ""
        for i in range(len(s)):
            char = s[i]
            if char.isdigit():
                num = num * 10 + int(char)
            
            elif char == '[':
                stack.append(num)
                num = 0
                stack.append(char)
            
            elif char == ']':
                while stack[-1] != '[':
                    string = stack.pop() + string
                stack.pop()
                k = stack.pop()
                stack.append(k*string)

                string = ""
            
            else:
                stack.append(char)
        
        res = ""
        while stack:
            res = stack.pop() + res
        
        return res


