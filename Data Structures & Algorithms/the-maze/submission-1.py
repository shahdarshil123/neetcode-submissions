class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        # 0 0 1 0 0
        # 0 0 0 0 0
        # 0 0 0 1 0
        # 1 1 0 1 1
        # 0 0 0 0 0 

        rows, columns = len(maze), len(maze[0])
        directions = [(0,1), (0,-1), (1,0), (-1,0)] # right, left, bottom, top
        visit = set()

        queue = collections.deque()
        queue.append((start[0], start[1]))

        def bfs(row, col):
            if (row, col) in visit:
                return
            for dr, dc in directions:
                r, c = row, col
                while r+dr >= 0 and r+dr < rows and c+dc >= 0 and c+dc < columns and maze[r+dr][c+dc] != 1:
                    r,c = r+dr, c+dc
                queue.append((r,c))
        
        while queue:
            r, c = queue.popleft()
            if r == destination[0] and c == destination[1]:
                return True
            bfs(r,c)
            visit.add((r,c))
        
        return False
                
                     
            
