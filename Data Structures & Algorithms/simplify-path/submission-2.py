class Solution:
    def simplifyPath(self, path: str) -> str:
        # /neetcode/practice//...///../courses

        stack = []
        cur = ""

        for char in path + "/":
            if char == "/":
                if cur == "..":
                    if stack:
                        stack.pop()
                elif not (cur == '.' or cur == ""):
                    stack.append(cur)
                cur = ""
            else:
                cur += char

        # print(stack) 
        return "/" + "/".join(stack)       
