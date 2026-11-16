class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        mheap = []            
        
        for i in range(len(points)):
            x = points[i][0]
            y = points[i][1]
            dist = math.sqrt(x*x + y*y)

            if i < k:
                heapq.heappush(mheap,(-dist,[x,y]))
            else:
                heapq.heappushpop(mheap, (- dist, [x,y]))
        
        res = []
        while mheap:
            val, point = heapq.heappop(mheap)
            res.append(point)
        
        return res

        

            


