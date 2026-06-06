class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        maxP = piles[0]
        for i in range(len(piles)):
            maxP = max(maxP,piles[i])
        low = 1
        high = maxP
        ans = 0
        while low <= high:
            mid = (low+high)//2
            if self.isFeasible(piles,mid,h):
                high = mid - 1
                ans = mid
            else:
                low = mid+1
        return ans
    
    def isFeasible(self,piles,mid,h):
        req = 0
        for elem in piles:
            if (elem//mid) < 1:
                req += 1
            else:
                if elem % mid != 0:
                    req += (elem//mid)+1
                else:
                    req += elem//mid
        return req <= h



        