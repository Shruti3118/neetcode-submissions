class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        visited = set()
        visited.add((points[0][0],points[0][1]))

        minheap = []

        for u, v in points:
            if (u,v) not in visited:
                weight = abs(points[0][0] - u) + abs(points[0][1] - v)
                heapq.heappush(minheap, (weight, u, v))
        
        total_weight = 0
        
        while minheap and len(visited) < len(points):
            weight, u, v = heapq.heappop(minheap)

            if (u,v) in visited:
                continue
            
            visited.add((u,v))
            total_weight += weight

            for point in points:
                if (point[0], point[1]) not in visited:
                    weight = abs(point[0] - u) + abs(point[1] - v)
                    heapq.heappush(minheap, (weight, point[0], point[1]))
            
        return total_weight
