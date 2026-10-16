class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        memo = [[-1]*len(nums) for _ in range(len(nums))]
        def dfs(i, prev):

            if i == len(nums):
                return 0
            
            if memo[i][prev] == -1:
                res = 0
                if prev == -1 or nums[prev] < nums[i]:
                    res = max(1+dfs(i+1,i),dfs(i+1,prev))
                else:
                    res = dfs(i+1,prev)
                
                memo[i][prev] = res
            
            return memo[i][prev]
        
        return dfs(0,-1)