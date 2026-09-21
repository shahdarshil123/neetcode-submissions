class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        directions = [(0,1),(1,0)]
        cache = {}
        def dfs(row,col):
            if row == m-1 and col == n-1:
                return 1
            if row < 0 or row >= m or col < 0 or col >= n:
                return 0
            if (row,col) in cache:
                return cache[(row,col)]
            cache[(row,col)] = 0
            for dr, dc in directions:
               cache[(row,col)] += dfs(row+dr, col+dc)
            return cache[(row,col)]
        
        return dfs(0,0)


            
            