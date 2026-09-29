class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        """
        def rec(n):
            if n == len(cost):
                return 0
            
            if n > len(cost):
                return float('inf')
            
            ans = min(cost[n]+rec(n+1), cost[n]+rec(n+2))

            return ans
        
        return min(rec(0), rec(1))
        """

        memo = [-1]*(len(cost)+1)
        
        def rec_memo(n):
            if n > len(cost):
                return float('inf')

            if memo[n] == -1:
                res = 0
                if n == len(cost):
                    res = 0
                
                else:
                    res = min(cost[n] + rec_memo(n+1), cost[n] + rec_memo(n+2))
                memo[n] = res
            
            return memo[n]
        
        return min(rec_memo(0), rec_memo(1))



                