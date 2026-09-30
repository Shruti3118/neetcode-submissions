class Solution:
    def rob(self, nums: List[int]) -> int:

        """

        memo = [-1]*(len(nums))

        def rec_memo(n):
            if n >= len(nums):
                return 0
            if memo[n] == -1:
                res = max(nums[n] + rec_memo(n+2), rec_memo(n+1))
                memo[n] = res
            
            return memo[n]
        
        return max(rec_memo(0), rec_memo(1))
        """

        def rec_tab():
            tab = [-1]*(len(nums))

            tab[len(nums)-1] = nums[len(nums)-1]

            tab[len(nums)-2] = max(nums[len(nums)-2], tab[len(nums)-1])

            for i in range(len(nums)-3,-1,-1):
                tab[i] = max(nums[i] + tab[i+2], tab[i+1])
            
            if len(nums) == 1:
                return tab[0]
                
            return max(tab[0], tab[1])
        
        return rec_tab()



                