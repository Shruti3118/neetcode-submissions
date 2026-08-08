class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        minheap = nums[:k]
        heapq.heapify(minheap)
        for x in nums[k:]:
            heapq.heappushpop(minheap,x)
        return minheap[0]
