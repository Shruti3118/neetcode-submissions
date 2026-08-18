class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        self.root = TrieNode()
        def insert(word):
            node = self.root
            for ch in word:
                if not node.child[ord(ch)-ord('a')]:
                    node.child[ord(ch)-ord('a')] = TrieNode()
                node = node.child[ord(ch)-ord('a')]
            node.isEnd = True
        
        for word in words:
            insert(word)
        
        res = set()
        ans = []

        visited = [[False] * len(board[0]) for i in range(len(board))]
        
        def dfs(root,row,col):
            if root.isEnd:
                res.add("".join(ans))
                
            if row == -1 or row == len(board):
                return
            
            if col == -1 or col == len(board[0]):
                return
            
            if visited[row][col]:
                return

            if not root.child[ord(board[row][col]) - ord('a')]:
                return
            
            ans.append(board[row][col])
            visited[row][col] = True

            dfs(root.child[ord(board[row][col])-ord('a')],row-1,col)
            dfs(root.child[ord(board[row][col])-ord('a')],row+1,col)
            dfs(root.child[ord(board[row][col])-ord('a')],row,col+1)
            dfs(root.child[ord(board[row][col])-ord('a')],row,col-1)
            
            ans.pop()
            visited[row][col] = False
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                dfs(self.root,i,j)
        
        return list(res)

class TrieNode:
    def __init__(self):
        self.child = [None]*26
        self.isEnd = False

        