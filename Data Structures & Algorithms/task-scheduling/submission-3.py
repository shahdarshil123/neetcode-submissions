class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freqMap = {}
        time = 0
        for task in tasks:
            freqMap[task] = freqMap.get(task,0) + 1
        
        queue = collections.deque()
        heap = []

        for k,v in freqMap.items():
            heap.append((-1*v, k)) # max heap of freq, task
        
        heapq.heapify(heap)
        
        while heap or queue:
            while queue and time == queue[0][2]:
                freq, task, timestamp = queue.popleft()
                heapq.heappush(heap, (freq, task))
            
            if heap:
                freq, task = heapq.heappop(heap) # freq, task
                if freq + 1 < 0:
                    queue.append((freq+1, task, time+n+1))
            
            time += 1
        
        return time


        

