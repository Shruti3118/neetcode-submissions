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
            tab = [-1]*len(s)

            if len(s) == 1 and s[0] != "0":
                return 1
            
            if len(s) == 1:
                return 0
            
            if len(s) == 0:
                return 0

            tab[len(s)-1] = 1 if s[-1] != "0" else 0
            
            if s[len(s)-2] == "0":
                tab[len(s)-2] = 0
            elif int(s[len(s)-2:]) == 10 or int(s[len(s)-2:]) == 20:
                tab[len(s)-2] = 1
            elif int(s[len(s)-2:]) <= 26:
                tab[len(s)-2] = 2
            else:
                tab[len(s)-2] = 1 

            for i in range(len(s)-3,-1,-1):
                
                if s[i] == "0":
                    tab[i] = 0
                elif int(s[i:i+2]) <= 26:
                    tab[i] = tab[i+1] + tab[i+2]
                else:
                    tab[i] = tab[i+1]

            return tab[0] 
        
        return rec_tab()

            

