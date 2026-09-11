class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        time = 0
        visited = set()
        count = 0
        heap = []

        # create adj list
        adjList = {i: [] for i in range(1,n+1)}
        for u,v,t in times:
            adjList[u].append((v,t))
        
        heap.append((0,k))


        while heap and count != n:
            time, node = heapq.heappop(heap)
            if node in visited:
                continue
            visited.add(node)
            count += 1
            for nei_node,nei_time in adjList[node]:
                heapq.heappush(heap, (time + nei_time, nei_node))
        
        if count != n:
            return -1
        return time
