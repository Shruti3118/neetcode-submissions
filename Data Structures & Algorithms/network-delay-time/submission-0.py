class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        dist = [float('inf')]*n
        dist[k - 1] = 0 
        minheap = []

        adjList = defaultdict(list)

        for u, v, w in times:
            adjList[u - 1].append((v - 1, w))

        heapq.heappush(minheap,(0, k - 1))

        while minheap:
            current_dist, node = heapq.heappop(minheap)

            if current_dist > dist[node]:
                continue
            
            for v, w in adjList[node]:
                
                if dist[node] + w < dist[v]:
                    dist[v] = dist[node] + w
                    heapq.heappush(minheap, (dist[v], v))
        
        maxTime = 0
        for i in range(len(dist)):
            maxTime = max(maxTime, dist[i])
        
        if maxTime == float('inf'):
            return -1
        
        return maxTime



