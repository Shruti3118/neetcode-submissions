class PrefixTree:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for ch in word:
            if not node.child[ord(ch)-ord('a')]:
                node.child[ord(ch)-ord('a')] = TrieNode()
            node = node.child[ord(ch)-ord('a')]
        node.isEnd = True

    def search(self, word: str) -> bool:
        node = self.root
        for ch in word:
            if not node.child[ord(ch)-ord('a')]:
                return False
            node = node.child[ord(ch)-ord('a')]
        return node.isEnd   

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for ch in prefix:
            if not node.child[ord(ch)-ord('a')]:
                return False
            node = node.child[ord(ch)-ord('a')]
        return True
        
class TrieNode:
    def __init__(self):
        self.child = [None]*26
        self.isEnd = False       