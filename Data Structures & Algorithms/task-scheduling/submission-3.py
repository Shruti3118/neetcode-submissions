class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        hm = {}
        for elem in tasks:
            hm[elem] = hm.get(elem,0) + 1
        maxheap = []
        for key in hm:
            maxheap.append(- hm[key])
        heapq.heapify(maxheap)
        print(maxheap)
        time = 0
        q = deque()
        while maxheap or q:
            time += 1
            if maxheap:
                count = 1 + heapq.heappop(maxheap)
                if count:
                    q.append([count,time+n])
            if q and q[0][1] == time:
                count, time = q.popleft()
                heapq.heappush(maxheap,count)
        return time