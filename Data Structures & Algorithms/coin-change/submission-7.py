class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        def dfs(i, total):
            if total == amount:
                return 0
            if total > amount:
                return float('inf')
            if (i,total) in memo:
                return memo[(i,total)]

            memo[(i,total)] = float('inf')
            for j in range(i, len(coins)):
                memo[(i,total)]  = min(memo[(i,total)] , 1 + dfs(j, total+coins[j]))
            return memo[(i,total)] 
        
        val = dfs(0,0)
        if val == float('inf'):
            return -1
        return val
    

                    