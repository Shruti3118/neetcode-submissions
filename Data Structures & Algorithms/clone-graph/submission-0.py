"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        if not node:
            return node

        visited = {}
        
        def dfs(u):
            if u in visited:
                return visited[u]
               
            newNode = Node(u.val)
            visited[u] = newNode

            for v in u.neighbors:
                newNode.neighbors.append(dfs(v))
                    
            return newNode
        
        return dfs(node)


                
            



        