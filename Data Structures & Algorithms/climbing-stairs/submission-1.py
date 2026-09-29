class Solution:
    def climbStairs(self, n: int) -> int:

        """
        def rec(n):
            if n < 0:
                return 0
            if n == 0:
                return 1
            
            return rec(n-1) + rec(n-2)
        """
        
        
        memo = [-1]*(n+1)

        def rec_memo(n):
            if memo[n] == -1:
                res = 0

                if n == 0:
                    res = 1
                
                elif n < 0:
                    res = 0
                
                else:
                    res = rec_memo(n-1) + rec_memo(n-2)

                memo[n] = res
            
            return memo[n]

        return rec_memo(n)
                

                

        