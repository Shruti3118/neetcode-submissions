class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        adjlist = defaultdict(list)
        indegree = [0]*numCourses

        for i,j in prerequisites:
            adjlist[j].append(i)
            indegree[i] += 1
        
        q = deque()
        
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
        
        res = []
        courses = 0

        while q:
            node = q.popleft()
            res.append(node)
            courses += 1

            for i in adjlist[node]:
                indegree[i] -= 1
                if indegree[i] == 0:
                    q.append(i)
            
        if courses != numCourses:
            return []
        
        return res
        