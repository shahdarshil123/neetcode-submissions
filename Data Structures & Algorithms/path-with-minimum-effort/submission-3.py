class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        # using bfs and dijikstra's algorithm
        rows, columns = len(heights), len(heights[0])
        heap = []
        visit = set()

        heap.append((0,0,0)) # (effort,row,col)
        # visit.add((0,0)) # (row, col)
        
        directions = [(0,1), (0,-1), (1,0), (-1,0)]

        max_effort = -float('inf') 
        while heap:
            eff,r,c = heapq.heappop(heap)
            visit.add((r, c))
            max_effort = max(max_effort, eff)
            if r == rows-1 and c == columns - 1:
                return max_effort
            for dr,dc in directions:
                if 0 <= r+dr < rows and 0 <= c+dc < columns and (r+dr,c+dc) not in visit:
                    effort = abs(heights[r+dr][c+dc] - heights[r][c])
                    heapq.heappush(heap, (effort, r+dr, c+dc))
                    
        
        return max_effort




        