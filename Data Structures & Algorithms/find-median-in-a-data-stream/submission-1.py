class MedianFinder:

    def __init__(self):
        self.maxheap = []
        self.minheap = []

    def addNum(self, num: int) -> None:
        if len(self.maxheap) < 1:
            heapq.heappush(self.maxheap,- num)
            return
        maxL = len(self.maxheap)
        minL = len(self.minheap)
        if - self.maxheap[0] >= num:
            if maxL - minL == 1:
                elem = - heapq.heappop(self.maxheap)
                heapq.heappush(self.minheap,elem)
            heapq.heappush(self.maxheap,- num)
        else:
            if maxL == minL:
                if self.minheap[0] > num:
                    heapq.heappush(self.maxheap,- num)
                    return
                elem = heapq.heappop(self.minheap)
                heapq.heappush(self.maxheap,- elem)
            heapq.heappush(self.minheap,num)
            
    def findMedian(self) -> float:
        minL = len(self.minheap)
        maxL = len(self.maxheap)
        if minL == maxL:
            return (self.minheap[0] - self.maxheap[0])/2
        return float(- self.maxheap[0])
        
        