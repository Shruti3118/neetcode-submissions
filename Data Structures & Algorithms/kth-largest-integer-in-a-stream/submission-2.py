import heapq
class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.minheap = nums[:k]
        heapq.heapify(self.minheap)
        for x in nums[k:]:
            if x > self.minheap[0]:
                heapq.heappushpop(self.minheap,x)

    def add(self, val: int) -> int:
        if len(self.minheap) < self.k:
            heapq.heappush(self.minheap,val)

        elif val > self.minheap[0]:
            heapq.heappushpop(self.minheap,val)
            
        return self.minheap[0]
        

        
        
