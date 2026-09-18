class Solution:
    def climbStairs(self, n: int) -> int:
        num1 = 1
        num2 = 0

        for i in range(n):
            t = num1
            num1 = num1 + num2
            num2 = t
        
        return num1
