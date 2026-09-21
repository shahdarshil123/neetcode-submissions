class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        rows, columns = len(grid), len(grid[0])
        directions = [(0,1), (1,0)]
        memo = {}

        def dfs(row, col):
            if row == rows-1 and col == columns-1:
                return grid[row][col]
            if row < 0 or row >= rows or col < 0 or col >= columns:
                return float('inf')
            if (row, col) in memo:
                return memo[(row, col)]
            val = float('inf')
            for dr, dc in directions:
                val = min(val, grid[row][col] + dfs(row+dr, col+dc))
            memo[(row, col)] = val
            return val
        
        return dfs(0,0)