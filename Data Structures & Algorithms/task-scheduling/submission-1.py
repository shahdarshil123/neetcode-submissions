class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        time = 0
        heap = []
        queue = collections.deque()

        count = {}
        for task in tasks:
            count[task] = count.get(task,0) + 1
        
        for k,v in count.items():
            heap.append((-1*v,k))  # freq, task
        
        heapq.heapify(heap)

        while heap or queue:
            while queue and time == queue[0][2]:
                freq, task, timestamp = queue.popleft() #freq, task, timestamp
                heapq.heappush(heap, (freq, task))
            
            if heap:
                freq, task = heapq.heappop(heap)
                if freq + 1 < 0:
                    queue.append((freq+1,task,time+n+1))
            
            time += 1
        
        return time