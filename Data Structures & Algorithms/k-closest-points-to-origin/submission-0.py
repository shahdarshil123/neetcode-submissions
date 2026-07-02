class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        result = []
        for point in points:
            distance = math.sqrt((point[0]**2 + point[1]**2))
            heapq.heappush(heap, (distance, point))
        
        for i in range(k):
            dist, point = heapq.heappop(heap)
            result.append(point)
        
        return result
        

