class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        rows, columns = len(matrix), len(matrix[0])
        directions = [(0,1), (0,-1), (1,0), (-1,0)]
        cache = {}

        def dfs(row, col):
            if (row, col) in cache:
                return cache[(row, col)]

            res = 1
            for dr, dc in directions:
                nr, nc = row + dr, col + dc
                if 0 <= nr < rows and 0 <= nc < columns and matrix[nr][nc] > matrix[row][col]:
                    res = max(res, 1 + dfs(nr, nc))
            cache[(row, col)] = res
            return res
        
        result = 0
        for row in range(rows):
            for col in range(columns):
                result = max(result, dfs(row, col))
        
        return result