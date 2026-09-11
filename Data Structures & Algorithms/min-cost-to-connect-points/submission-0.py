class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        adjList = {i:[] for i in range(n)}
        
        for i in range(n-1):
            x1,y1 = points[i]
            for j in range(i+1,n):
                x2,y2 = points[j]
                dist = abs(x1-x2) + abs(y1-y2)
                adjList[i].append((j, dist))
                adjList[j].append((i,dist))
        
        heap = [(0,0)]  #dist, index
        visit = set()
        total_dist = 0

        while heap and len(visit) < n:
            dist, indx = heapq.heappop(heap)
            if indx in visit:
                continue
            
            visit.add(indx)
            total_dist += dist

            for nei, d in adjList[indx]:
                heapq.heappush(heap, (d, nei))
        
        return total_dist


        