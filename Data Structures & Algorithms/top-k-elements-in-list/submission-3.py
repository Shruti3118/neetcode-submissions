class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hm = {}
        for i in nums:
            hm[i] = hm.get(i,0)+1
        buckets = [[] for _ in range(len(nums)+1)]
        for i,count in hm.items():
            buckets[count].append(i)
        res = []
        for i in range(len(buckets)-1,0,-1):
            for num in buckets[i]:
                res.append(num)
                if len(res) == k:
                    return res

            
            

        
        
        