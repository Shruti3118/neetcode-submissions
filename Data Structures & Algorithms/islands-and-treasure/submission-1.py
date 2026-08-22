class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        visited = set()
        q = deque()
        inf = 2147483647

        def bfs():
            dist = 0
            while q:
                dist += 1
                for x in range(len(q)):
                    r,c = q.popleft()
                    
                    directions = [(-1,0),(1,0),(0,-1),(0,1)]

                    for dr, dc in directions:
                        if r + dr < 0 or r + dr == len(grid) or c + dc < 0 or c + dc == len(grid[0]):
                            continue
                        if grid[r+dr][c+dc] == inf:
                            grid[r+dr][c+dc] = dist
                            q.append((r+dr,c+dc))
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    q.append((i,j))
        
        bfs()



            
            
                    
            

            

                

                        



