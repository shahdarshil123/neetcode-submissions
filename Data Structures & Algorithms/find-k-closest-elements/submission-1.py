class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        heap = []
        for i in range(len(arr)):
            heap.append((abs(arr[i] - x), arr[i]))
        heapq.heapify(heap)

        result = []
        for i in range(k):
            val, num = heapq.heappop(heap)
            result.append(num)
        result.sort()
        return result
        