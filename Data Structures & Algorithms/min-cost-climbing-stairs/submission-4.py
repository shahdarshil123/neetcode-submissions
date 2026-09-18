class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        num1 = 0
        num2 = 0

        for i in range(len(cost)-1,-1,-1):
            t = num1
            num1 = cost[i] + min(num1, num2)
            num2 = t
        
        return min(num1, num2)

