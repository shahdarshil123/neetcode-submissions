class Solution:
    def decodeString(self, s: str) -> str:
        # using recursion:
        # use global indicator

        self.i = 0
        self.s = s

        def helper():
            res = ""
            num = 0

            while self.i < len(self.s):
                char = s[self.i]
                if char.isdigit():
                    num = num*10 + int(char)
                
                elif char == '[':
                    self.i += 1
                    res += num * helper()
                    num = 0

                
                elif char == ']':
                    return res
        
                
                else:
                    res += char

                self.i += 1
            return res
        
        return helper()
            

        