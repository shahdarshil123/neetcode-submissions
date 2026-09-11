class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)

        parent = {i:i for i in range(1,n+1)}
        rank = {i:1 for i in range(1,n+1)}

        def find(n):
            if parent[n] != n:
                parent[n] = find(parent[n])
            return parent[n]
        
        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
            if p1 == p2:        # cycle detection
                return False
            
            if rank[p1] >= rank[p2]:
                rank[p1] += rank[p2]
                parent[p2] = p1
            else:
                rank[p2] += rank[p1]
                parent[p1] = p2
            
            return True
        
        for edge in edges:
            n1, n2 = edge
            if not union(n1,n2):
                return edge

        return [] 