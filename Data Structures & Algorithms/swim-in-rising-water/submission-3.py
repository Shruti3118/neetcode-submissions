class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        
        def dfs(i,j,t,visited):
            if i < 0 or i > len(grid) - 1:
                return False
            
            if j < 0 or j > len(grid[0]) - 1:
                return False
            
            if t < grid[i][j]:
                return False

            if (i,j) in visited:
                return False
            
            if i == len(grid) - 1 and j == len(grid[0]) - 1:
                return True
            
            visited.add((i,j))

            return (dfs(i+1,j,t,visited) or dfs(i-1,j,t,visited) or dfs(i,j+1,t,visited) or dfs(i,j-1,t,visited))


        maxT = max(max(row) for row in grid) 
        minT = min(min(row) for row in grid)

        l = minT
        r = maxT
        res = maxT

        while l <= r:
            m = (l+r)//2

            visited = set()
            if dfs(0,0,m,visited):
                r = m - 1
                res = m
            
            else:
                l = m + 1
        
        return res

                
