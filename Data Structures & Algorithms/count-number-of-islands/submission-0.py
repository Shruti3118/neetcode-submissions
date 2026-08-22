class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        def bfs(r,c,visited):
            q = deque()

            q.append((r,c))
            visited.add((r,c))

            while q:
                r,c = q.popleft()
                directions = [(-1,0),(1,0),(0,1),(0,-1)]
                for dr,dc in directions:
                    if r + dr < 0 or r + dr == len(grid) or c + dc < 0 or c + dc == len(grid[0]):
                        continue
                    if grid[r + dr][c + dc] == "1" and (r + dr,c + dc) not in visited:
                        visited.add((r + dr,c + dc))
                        q.append((r + dr,c + dc))
        
        visited = set()
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1" and (i,j) not in visited:
                    bfs(i,j,visited)
                    count += 1
                    
        
        return count
