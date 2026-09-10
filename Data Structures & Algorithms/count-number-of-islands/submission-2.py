class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, columns = len(grid), len(grid[0])
        visited = set()

        def dfs(row, col):
            if row < 0 or row >= rows or col < 0 or col >= columns:
                return
            if (row, col) in visited:
                return
            if grid[row][col] == '0':
                return
            visited.add((row,col))

            dfs(row+1,col)
            dfs(row,col+1)
            dfs(row-1,col)
            dfs(row,col-1)

        islands = 0
        for row in range(rows):
            for col in range(columns):
                if grid[row][col] == '1' and (row, col) not in visited:
                    islands += 1
                    dfs(row, col)
        
        return islands







