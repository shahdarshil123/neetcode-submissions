class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # Approch
        # maintain a monotonic decreasing queue such that the maximum element is always at the start
        # for each index check if element at the start of queue is present in the window or not if not remove from the queue

        # create a queue and append the values
        queue = collections.deque()
        result = []
        left = 0
        for right in range(k):
            while queue and nums[queue[-1]] < nums[right]:
                queue.pop()
            queue.append(right)

        result.append(nums[queue[0]])

        right += 1
        while right < len(nums):
            left += 1
            if queue and queue[0] < left:
                queue.popleft()
            
            while queue and nums[queue[-1]] < nums[right]:
                queue.pop()
            queue.append(right)
            result.append(nums[queue[0]])
            right += 1
        
        return result
        

            


