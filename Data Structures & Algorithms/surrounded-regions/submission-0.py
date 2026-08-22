class Solution:
    def solve(self, board: List[List[str]]) -> None:

        visited = set()
        
        def dfs(r,c):
            visited.add((r,c))
            
            directions = [(-1,0),(1,0),(0,1),(0,-1)]
            for dr,dc in directions:
                if r + dr < 0 or r + dr == len(board) or c + dc < 0 or c + dc == len(board[0]):
                    continue
                if board[r+dr][c+dc] == "O" and (r+dr,c+dc) not in visited:
                    dfs(r+dr,c+dc)
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if (i == 0 or j == 0 or i == len(board) - 1 or j == len(board[0]) - 1) and board[i][j] == "O":
                        dfs(i,j)
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "O" and (i,j) not in visited:
                    board[i][j] = "X"
        



