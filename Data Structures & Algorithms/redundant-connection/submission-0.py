class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = {}
        rank = {}

        for i in range(1,len(edges)+1):
            parent[i] = i
            rank[i] = 0
        
        def find(x):
            if x == parent[x]:
                return x
            
            parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            x_rep = find(x)
            y_rep = find(y)

            if x_rep == y_rep:
                return True
            
            if rank[x_rep] < rank[y_rep]:
                parent[x_rep] = y_rep

            elif rank[y_rep] < rank[x_rep]:
                parent[y_rep] = x_rep
            
            else:
                parent[x_rep] = y_rep
                rank[y_rep] += 1
        
        i = 0
        while i < len(edges):
            u, v = edges[i]

            if union(u,v):
                return edges[i]
            
            i += 1
        
        return edges[i-1]
        
            



 
            
            