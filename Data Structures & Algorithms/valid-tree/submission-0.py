class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        visited = set()

        adjList = defaultdict(list)

        for i,j in edges:
            adjList[i].append(j)
            adjList[j].append(i)
        

        def dfs(i,parent):
            visited.add(i)

            for node in adjList[i]:
                if node not in visited:
                    ans = dfs(node,i)
                    if ans:
                        return True
                elif node != parent:
                    return True
            
            return False
        
        count = 0
        for i in range(n):
            if i not in visited:
                ans = dfs(i,-1)
                count += 1
                if ans:
                    return False
        
        return count == 1

