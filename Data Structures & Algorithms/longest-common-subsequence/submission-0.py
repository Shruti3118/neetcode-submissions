class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        dp = [[-1 for _ in range(len(text2))] for _ in range(len(text1))]
        
        def dfs(t1,t2):
            if t1 == len(text1) or t2 == len(text2):
                return 0
            
            if dp[t1][t2] == -1:
                res = 0
                if text1[t1] != text2[t2]:
                    res = max(dfs(t1+1,t2),dfs(t1,t2+1))
                else:
                    res = 1 + dfs(t1+1, t2+1)
                dp[t1][t2] = res

            return dp[t1][t2]

        return dfs(0,0) 




