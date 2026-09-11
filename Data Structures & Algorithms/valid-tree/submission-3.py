class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False

        parent = {i:i for i in range(n)}
        rank = {i:1 for i in range(n)}

        def find(n):
            if parent[n] != n:
                parent[n] = find(parent[n])
            return parent[n]
        
        def union(n1, n2):
            p1, p2 = find(n1), find(n2)

            if p1 == p2:
                return False
            
            if rank[p1] >= rank[p2]:
                rank[p1] += rank[p2]
                parent[p2] = p1
            else:
                rank[p2] += rank[p1]
                parent[p1] = p2
            
            return True

        for n1, n2 in edges:
            if not union(n1, n2):
                return False
        
        return True