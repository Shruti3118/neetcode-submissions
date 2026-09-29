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

        """
        Memoization solution

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
        """

        def rec_tab():
            tab = [-1]*(len(cost)+1)

            tab[len(cost)] = 0

            for i in range(len(cost)-1,-1,-1):
                if i == len(cost) - 1:
                    tab[i] = tab[i+1] + cost[i]
                else:
                    tab[i] = min(tab[i+1] + cost[i], tab[i+2] + cost[i])
            
            return min(tab[0], tab[1])
        
        return rec_tab()





                