class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjList = defaultdict(list)
        indegrees = [0]*numCourses

        for i,j in prerequisites:
            adjList[j].append(i)
            indegrees[i] += 1
        
        q = deque()

        for i in range(numCourses):
            if indegrees[i] == 0:
                q.append(i)

        courses = 0

        while q:
            node = q.popleft()
            courses += 1

            for i in adjList[node]:
                indegrees[i] -= 1
                if indegrees[i] == 0:
                    q.append(i)

        return courses == numCourses    