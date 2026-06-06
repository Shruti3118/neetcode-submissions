class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            s = set()
            for j in range(9):
                if board[i][j] == ".":
                    continue
                if board[i][j] in s:
                    return False
                s.add(board[i][j])
        for j in range(9):
            s = set()
            for i in range(9):
                if board[i][j] == ".":
                    continue
                if board[i][j] in s:
                    return False
                s.add(board[i][j])
        x1=y1=0
        x2=y2=3
        while x2<=9 and y2<=9:
            s = set()
            for i in range(x1,x2):
                for j in range(y1,y2):
                    if board[i][j] == ".":
                        continue
                    if board[i][j] in s:
                        return False
                    s.add(board[i][j])
            x1+=3
            x2+=3
            if x1 == 9:
                x1=0
                x2=3
                y1+=3
                y2+=3
        return True


            
                
                