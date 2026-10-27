class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        if sum(nums) % 2 != 0:
            return False
        
        target = sum(nums) // 2
        
        dp = [False]*(target+1)

        dp[0] = True

        for i in nums:
            for j in range(target,i-1,-1):
                dp[j] = dp[j] or dp[j-i]
        
        return dp[target]

        
        

                    