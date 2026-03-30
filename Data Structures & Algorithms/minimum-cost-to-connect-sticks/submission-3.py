class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        heap = [stick for stick in sticks]
        heapq.heapify(heap)
        res = 0

        while len(heap) > 1:
            num1 = heapq.heappop(heap)
            num2 = heapq.heappop(heap)
            num = num1 + num2
            res += num
            heapq.heappush(heap, num)
        
        return res


