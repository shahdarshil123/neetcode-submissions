class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        
        # conditions to check if town judge exists:
        # 1. There is only one person who doesn't trust anybody
        # 2. That person is being trusted by everybody else

        adjList = {i:[] for i in range(1,n+1)}
        for a,b in trust:
            adjList[a].append(b)

        def check_judge(judge):
            for p in range(1,n+1):
                if p != judge and judge not in adjList[p]:
                    return False
            return True


        for judge in range(1, n+1):
            if len(adjList[judge]) == 0:
                if check_judge(judge):
                    return judge
        return -1
                    

                    
