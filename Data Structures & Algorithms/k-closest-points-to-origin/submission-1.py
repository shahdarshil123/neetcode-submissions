import math

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for point in points:
            x, y = point[0], point[1]
            dist = math.sqrt((x-0)**2 +(y-0)**2)
            heap.append((dist, point))
        
        heapq.heapify(heap)
        result = []
        while heap and k > 0:
            dist, point = heapq.heappop(heap)
            result.append(point)
            k -= 1
        
        return result
