class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # [[1,0]]: 1-> 0
        result = []

        # create adj list
        adjList = {courses: [] for courses in range(numCourses)}
        for course,preq in prerequisites:
            adjList[course].append(preq)
        
        # run topological sort
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
            result.append(course)
            return True
        
        for course in range(numCourses):
            if not dfs(course):
                return []
        return result
            
                

