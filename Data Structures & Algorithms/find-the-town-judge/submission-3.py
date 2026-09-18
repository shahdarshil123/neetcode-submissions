class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trustMap = {i:[0,0] for i in range(1,n+1)} #[incoming, outgoing]
        for a,b in trust:
            trustMap[a][1] += 1
            trustMap[b][0] += 1
        
        for p in range(1, n+1):
            if trustMap[p][0] == n-1 and trustMap[p][1] == 0:
                return p
        return -1
