class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        open = 0
        close = 0
        arr = []
        result = []

        def dfs(open, close):
            if close > open or open > n:
                return
            
            if open == close == n:
                result.append("".join(arr))
                return
                
            
            arr.append('(')
            dfs(open+1, close)
            arr.pop()
            arr.append(')')
            dfs(open,close+1)
            arr.pop()
        
        dfs(0,0)
        return result
