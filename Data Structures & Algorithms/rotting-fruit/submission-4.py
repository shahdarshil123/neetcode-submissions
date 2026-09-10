class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, columns = len(grid), len(grid[0])

        queue = collections.deque()
        time = 0
        directions = [(0,1), (0,-1), (1,0), (-1,0)]
        visited = set()
        fruits = 0
        
        for row in range(rows):
            for col in range(columns):
                if grid[row][col] == 1:
                    fruits += 1
                elif grid[row][col] == 2:
                    queue.append((row,col))
                    visited.add((row,col))
        
        while queue and fruits > 0:
            for _ in range(len(queue)):
                r, c = queue.popleft()
                for dr, dc in directions:
                    if  0 <= r+dr < rows and 0<=c+dc < columns and (r+dr, c+dc) not in visited and grid[r+dr][c+dc] == 1:
                        queue.append((r+dr, c+dc))
                        visited.add((r+dr, c+dc))
                        fruits -= 1
            time += 1
        
        if fruits == 0:
            return time
        return -1