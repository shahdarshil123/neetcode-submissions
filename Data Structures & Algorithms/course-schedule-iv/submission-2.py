class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        # Track reachability for each course
        adjList = {i:[] for i in range(numCourses)}
        for pre, course in prerequisites:
            adjList[course].append(pre)
         
        prereqs = {i: set() for i in range(numCourses)}
        visit = set()

        def dfs(course):
            if course in visit:
                return prereqs[course]
            for nei_course in adjList[course]:
                prereqs[course].add(nei_course)
                prereqs[course].update(dfs(nei_course))
            visit.add(course)
            return prereqs[course]
        
        for course in range(numCourses):
            dfs(course)
        
        result = []
        for pre, course in queries:
            result.append(pre in prereqs[course])

        return result