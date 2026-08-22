class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()

        def bfs(countFresh,dist):
            visited = set()  
            while q and countFresh > 0:
                for x in range(len(q)):
                    r , c = q.popleft()
                    directions = [(-1,0),(1,0),(0,1),(0,-1)]
                    for dr,dc in directions:
                        if r + dr < 0 or r + dr == len(grid) or c + dc < 0 or c + dc == len(grid[0]):
                            continue
                        if grid[r+dr][c+dc] == 1 and (r+dr,c+dc) not in visited:
                            countFresh -= 1
                            print(countFresh)
                            visited.add((r+dr,c+dc))
                            q.append((r+dr,c+dc))
                dist += 1
            
            return (countFresh,dist)
        
        countFresh = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    countFresh += 1
                elif grid[i][j] == 2:
                    q.append((i,j))
        print(countFresh)
        countF, minutes = bfs(countFresh,0)
        print(countF)
        print(minutes)
        if countF == 0:
            return minutes
        return -1

                            

