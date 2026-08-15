class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        visited = [[False]*len(board[0]) for i in range(len(board))]
        def backtrack(row,col,i):
            if i == len(word):
                return True
            
            if row == -1 or row == len(board):
                return False
            
            if col == -1 or col == len(board[0]):
                return False
            
            if visited[row][col]:
                return False
            
            if word[i] != board[row][col]:
                return False
            
            visited[row][col] = True
            ans = backtrack(row - 1, col,i+1) or backtrack(row+1, col,i+1) or backtrack(row,col+1,i+1) or backtrack(row,col-1,i+1)
            
            if ans:
                return ans
            visited[row][col] = False

            return False
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if backtrack(i,j,0):
                    return True
        
        return False




