class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        self.area = 0

        def dfs(r,c,visited):
            visited.add((r,c))
            self.area += 1

            directions = [(-1,0),(1,0),(0,-1),(0,1)]
            for dr, dc in directions:
                if r + dr < 0 or r + dr == len(grid) or c + dc < 0 or c + dc == len(grid[0]):
                    continue
                if grid[r+dr][c+dc] == 1 and (r+dr,c+dc) not in visited:
                    dfs(r+dr,c+dc,visited)
        ans = 0
        visited = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1 and (i,j) not in visited:
                    self.area = 0
                    dfs(i,j,visited)
                    ans = max(self.area,ans)
        
        return ans
            
