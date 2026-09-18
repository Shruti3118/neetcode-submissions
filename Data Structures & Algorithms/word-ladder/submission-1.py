class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        
        wordList.append(beginWord)


        i = 0

        adjList = defaultdict(list)

        while i < len(wordList):
            
            start = wordList[i] 

            for word in wordList:
                count = 0
                for j in range(len(start)):
                    if word[j] != start[j]:
                        count += 1
                    if count > 1:
                        break
                if count == 1:
                    adjList[start].append(word)
            
            i += 1
        
        queue = deque()
        visited = set()

        dist = {word: float('inf') for word in wordList}

        visited.add(beginWord)
        queue.append(beginWord)
        dist[beginWord] = 0

        while queue:
            node = queue.popleft()

            for word in adjList[node]:
                if word not in visited:
                    queue.append(word)
                    visited.add(word)
                    dist[word] = 1 + dist[node]
        
        if dist[endWord] == float('inf'):
            return 0
        return dist[endWord]+1
                    
        

        

        
        


        









        