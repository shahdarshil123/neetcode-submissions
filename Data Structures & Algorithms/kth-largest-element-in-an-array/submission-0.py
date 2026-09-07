class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Create a max heap
        heap = [-1* num for num in nums]
        heapq.heapify(heap)

        while heap and k > 0:
            num = heapq.heappop(heap)
            k -= 1
        
        return -1 * num

