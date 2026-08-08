class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxheap = [- x for x in stones]
        heapq.heapify(maxheap)
        while len(maxheap) > 1:
            stone1 = - heapq.heappop(maxheap)
            stone2 = - heapq.heappop(maxheap)
            if stone1 - stone2 > 0:
                heapq.heappush(maxheap,-(stone1-stone2))
        return - maxheap[0] if len(maxheap) > 0 else 0
        

        