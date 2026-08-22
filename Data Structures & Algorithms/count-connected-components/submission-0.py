class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adjList = defaultdict(list)
        for a,b in edges:
            adjList[a].append(b)
            adjList[b].append(a)
        
        visited = set()
        
        def dfs(i):
            visited.add(i)

            for node in adjList[i]:
                if node not in visited:
                    dfs(node)
        
        count = 0
        for i in range(n):
            if i not in visited:
                dfs(i)
                count += 1
        
        return count


        

