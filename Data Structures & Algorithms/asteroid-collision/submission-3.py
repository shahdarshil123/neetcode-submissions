class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for ast in asteroids:
            if ast < 0:
                while stack and stack[-1] > 0 and stack[-1] < -1 * ast:
                    stack.pop()
                if stack and stack[-1] > 0 and stack[-1] == -1 * ast:
                    stack.pop()
                    continue
                elif stack and stack[-1] > 0 and stack[-1] > -1 * ast:
                    continue
            stack.append(ast)
        return stack