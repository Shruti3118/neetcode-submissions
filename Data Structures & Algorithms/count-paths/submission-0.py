class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        dp = [[-1 for _ in range(n)] for _ in range(m)]

        def dfs(x, y):
            if x == m - 1 and y == n - 1:
                return 1
            if x == m:
                return 0
            if y == n:
                return 0
            
            if dp[x][y] == -1:
                
                res = dfs(x+1,y) + dfs(x, y+1)

                dp[x][y] = res
            
            return dp[x][y]
        
        return dfs(0, 0)