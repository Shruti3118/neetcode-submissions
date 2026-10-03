class Solution:
    def numDecodings(self, s: str) -> int:


        """
        memo = [-1]*len(s)
        
        def rec_memo(j):
            if j == len(s):
                return 1
            
            if j > len(s):
                return 0
            
            if s[j] == "0":
                return 0
            
            if memo[j] == -1:
                res = 0

                if s[j] != "1" and s[j] != "2":
                    res = rec_memo(j+1)

                else:
                    if j+1 < len(s) and int(s[j:j+2]) <= 26:
                        res = rec_memo(j+1) + rec_memo(j+2)
                    else:
                        res = rec_memo(j+1)
                
                memo[j] = res
            
            return memo[j]
        
        return rec_memo(0)
        """

        def rec_tab():
            tab = [-1]*(len(s)+1)

            tab[len(s)] = 1

            for i in range(len(s)-1,-1,-1):
                if s[i] == "0":
                    tab[i] = 0
                
                elif i + 1 < len(s) and int(s[i:i+2]) <= 26:
                    tab[i] = tab[i+1] + tab[i+2]
                
                else:
                    tab[i] = tab[i+1]
            
            return tab[0]
        
        return rec_tab()
            


            

