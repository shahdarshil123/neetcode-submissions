class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
    
        adjList = {i: [] for i in range(numCourses)}
        for course, preq in prerequisites:
            adjList[course].append(preq)
        
        visit = set()
        path = set()
        
        def dfs(course):
            if course in path:
                return False
            if course in visit:
                return True
            path.add(course)
            for preq in adjList[course]:
                if not dfs(preq):
                    return False
            path.remove(course)
            visit.add(course)
            return True
        
        for course in range(numCourses):
            if not dfs(course):
                return False
        return True
