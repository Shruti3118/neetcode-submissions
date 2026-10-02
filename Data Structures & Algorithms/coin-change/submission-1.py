class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        """
        memo = [-1]*(amount+1)

        def rec_memo(amt):
            if amt < 0:
                return float('inf')

            if amt == 0:
                return 0
            
            if memo[amt] == -1:
                res = float('inf')
                for i in range(len(coins)):
                    res = min(res, rec_memo(amt - coins[i]) + 1)
                
                memo[amt] = res
            
            return memo[amt]

        if rec_memo(amount) == float('inf'):
            return -1
        return rec_memo(amount)
        """

        def rec_tab():
            tab = [float('inf')]*(amount+1)

            tab[0] = 0

            for i in range(1,amount+1):
                
                for j in range(len(coins)):
                    if i - coins[j] >= 0:
                        tab[i] = min(tab[i - coins[j]] + 1, tab[i])
            
            if tab[amount] == float('inf'):
                return -1
            
            return tab[amount]
        
        return rec_tab()
