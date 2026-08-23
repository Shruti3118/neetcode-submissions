class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific = set()
        atlantic = set()

        def dfs(r,c,visit):
            visit.add((r,c))
            
            directions = [(-1,0),(1,0),(0,-1),(0,1)]
            for dr, dc in directions:
                if r + dr < 0 or c + dc < 0 or r + dr == len(heights) or c + dc == len(heights[0]) or (r+dr,c+dc) in visit:
                    continue
                if heights[r][c] > heights[r+dr][c+dc]:
                    continue
                dfs(r+dr,c+dc,visit)     

        for i in range(len(heights)):
            dfs(i,0,pacific)
            dfs(i,len(heights[0])-1,atlantic)

        for j in range(len(heights[0])):
            dfs(0,j,pacific)
            dfs(len(heights)-1,j,atlantic)
        
        res = []
        for i in range(len(heights)):
            for j in range(len(heights[0])):
                if (i,j) in pacific and (i,j) in atlantic:
                    res.append([i,j])
        
        return res
        
        
        
        



                