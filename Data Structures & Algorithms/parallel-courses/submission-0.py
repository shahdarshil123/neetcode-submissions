class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        # relations [prev, curr]
        adjList = {i:[] for i in range(n+1)}

        for prev, curr in relations:
            adjList[curr].append(prev)
        
        visit = set()

        cache = {}
        def dfs(course):
            if course in visit:
                return float('inf')
            if len(adjList[course]) == 0:
                return 1
            if course in cache:
                return cache[course]
            visit.add(course)
            pre_sems = 0
            for pre_course in adjList[course]:
                pre_sems = max(pre_sems, dfs(pre_course))
            visit.remove(course)
            cache[course] = 1 + pre_sems
            return cache[course]
        
        minSems = 0
        for course in range(1,n+1):
            minSems = max(minSems, dfs(course))
        
        return -1 if minSems == float('inf') else minSems
