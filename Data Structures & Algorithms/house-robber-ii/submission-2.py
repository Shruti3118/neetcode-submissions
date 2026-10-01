class Solution:
    def rob(self, nums: List[int]) -> int:

        def rec(n,arr):
            memo = [-1]*(len(nums) - 1)

            def rec_memo(n,arr):
                if n >= len(arr):
                    return 0
                
                if memo[n] == -1:
                    res = max(arr[n] + rec_memo(n+2,arr), rec_memo(n+1,arr))
                    memo[n] = res
                
                return memo[n]

            return rec_memo(0,arr)
        
        if len(nums) == 1:
            return nums[0]
        
        return max(rec(0,nums[1:]), rec(0,nums[:-1]))
            