class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        
        wordList.append(beginWord)

        graph = defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i+1:]
                graph[pattern].append(word)
        
        queue = deque()
        queue.append(beginWord)
        visited = set()
        visited.add(beginWord)

        res = 0
        while queue:

            for i in range(len(queue)):
                node = queue.popleft()

                if node == endWord:
                    return res + 1

                for j in range(len(node)):
                    pattern = node[:j] + "*" + node[j+1:]

                    for word in graph[pattern]:
                        if word not in visited:
                            queue.append(word)
                            visited.add(word)
            
            res += 1
        
        return 0
            


            
                    
        

        

        
        


        









        