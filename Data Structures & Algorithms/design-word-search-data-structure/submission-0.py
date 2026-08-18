class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for ch in word:
            if not node.child[ord(ch)-ord('a')]:
                node.child[ord(ch)-ord('a')] = TrieNode()
            node = node.child[ord(ch)-ord('a')]
        node.isEnd = True
        
    def search(self, word: str) -> bool:

        def dfs(root,i):
            if i == len(word):
                return root.isEnd
            
            if word[i] != ".":
                if root.child[ord(word[i])-ord('a')]:
                    return dfs(root.child[ord(word[i])-ord('a')],i+1)
                return False
                    
            for j in range(len(root.child)):
                if root.child[j]:
                    ans = dfs(root.child[j],i+1)
                    if ans:
                        return True
            
            return False
        
        return dfs(self.root,0)



        

class TrieNode:
    def __init__(self):
        self.child = [None]*26
        self.isEnd = False