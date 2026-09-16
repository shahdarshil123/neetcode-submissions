class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        curr_people_count = 0
        heap = [] # (pickup/drop point val, from/to, people_count,)  from -> 0, to -> 1

        for i in range(len(trips)):
            trip = trips[i]
            people, source, dest = trip[0], trip[1], trip[2]
            heap.append((source,i,0,people)) # 
            heap.append((dest,i,1,people))
        
        heapq.heapify(heap)

        while heap:
            _, i, k, people = heapq.heappop(heap)
            if k == 0:
                curr_people_count += people
            elif k == 1:
                curr_people_count -= people
            
            if curr_people_count > capacity:
                return False
        
        return True
            

            
