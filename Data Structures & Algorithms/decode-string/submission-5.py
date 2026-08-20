class Solution:
    def decodeString(self, s: str) -> str:
        count_stack = []
        char_stack = []

        count = 0
        char_str = ""

        for char in s:
            if char.isdigit():
                count = count * 10 + int(char)

            elif char == '[':
                count_stack.append(count)
                char_stack.append(char_str)

                count = 0
                char_str = ""

            elif char == ']':
                previous = char_stack.pop()
                num = count_stack.pop()

                char_str = previous + char_str * num

            else:
                char_str += char 
            
        return char_str