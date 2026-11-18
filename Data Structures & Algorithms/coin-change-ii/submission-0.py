class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        dp = [[-1]*(len(coins)) for _ in range(amount+1)]

        def dfs(target,j):
            if target == 0:
                return 1
            
            if target < 0 or j == len(coins):
                return 0

            if dp[target][j] == -1:
                res = 0
                
                for i in range(j,len(coins)):
                    res += dfs(target - coins[i],i)
                
                dp[target][j] = res
            
            return dp[target][j]
        
        return dfs(amount, 0)