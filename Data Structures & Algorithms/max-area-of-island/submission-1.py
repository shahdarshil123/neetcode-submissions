class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # depth first search
        rows, columns = len(grid), len(grid[0])
        max_area = 0
        visited = set()

        def dfs(row, col):
            if row < 0 or row >= rows or col < 0 or col >= columns:
                return 0
            if (row, col) in visited:
                return 0
            if grid[row][col] == 0:
                return 0
            visited.add((row, col))
            
            return 1 + dfs(row+1,col) + dfs(row-1,col) + dfs(row, col+1) + dfs(row, col-1)

        for row in range(rows):
            for col in range(columns):
                if grid[row][col] == 1:
                   max_area = max(dfs(row, col), max_area)
        
        return max_area