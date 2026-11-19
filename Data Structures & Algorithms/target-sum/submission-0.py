class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        totSum = sum(nums)

        dp = [[-1 for _ in range(len(nums))] for _ in range(2*totSum + 1)]

        def dfs(targetSum, i):
            
            if i == len(nums):
                if targetSum == target + totSum:
                    return 1
                
                else:
                    return 0
            
            if dp[targetSum][i] == -1:

                res = dfs(targetSum + nums[i], i+1) + dfs(targetSum - nums[i],i+1)

                dp[targetSum][i] = res
            
            return dp[targetSum][i]
        
        return dfs(totSum, 0)