class Solution:
    def rob(self, nums: List[int]) -> int:

        memo = [-1]*(len(nums))

        def rec_memo(n):
            if n >= len(nums):
                return 0
            if memo[n] == -1:
                res = max(nums[n] + rec_memo(n+2), rec_memo(n+1))
                memo[n] = res
            
            return memo[n]
        
        return max(rec_memo(0), rec_memo(1))

                