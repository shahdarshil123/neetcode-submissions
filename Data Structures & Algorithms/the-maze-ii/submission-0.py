class Solution:
    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
        # use BFS
        rows, columns = len(maze), len(maze[0])
        directions = [(0,-1), (0,1), (-1,0), (1,0)]
        visit = set()

        queue = collections.deque() # dist, row, col
        queue.append((0,start[0], start[1]))
        visit.add((start[0], start[1]))

        while queue:
            for _ in range(len(queue)):
                dist, r, c =  queue.popleft()
                if r == destination[0] and c == destination[1]:
                    return dist
                for dr, dc in directions:
                    d = 0
                    r1 = r
                    c1 = c
                    while 0 <= r1+dr < rows and 0 <= c1+dc < columns and maze[r1+dr][c1+dc] != 1:
                        r1 = r1 + dr
                        c1 = c1 + dc
                        d += 1
                    if (r1,c1) not in visit:
                        queue.append((dist+d,r1,c1))
                        visit.add((r1,c1))
        
        return -1
                
