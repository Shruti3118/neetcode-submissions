class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        maxLen = 0
        for word in wordDict:
            maxLen = max(maxLen, len(word))

        wordSet = set(wordDict)

        """
        memo = [-1]*len(s)

        def dp_memo(i):

            if i == len(s):
                return True
            
            if memo[i] == -1:
                res = False

                for j in range(i,i+maxLen):
                    if s[i:j+1] in wordSet:
                        res = dp_memo(j+1)
                    
                    if res == True:
                        break
                
                memo[i] = res

            return memo[i]
        
        return dp_memo(0)
        """

        def dfs():
            tab = [False]*(len(s)+1)

            tab[len(s)] = True

            for i in range(len(s)-1,-1,-1):
                for j in range(i,min(i+maxLen,len(s))):
                    if s[i:j+1] in wordSet:
                        tab[i] = tab[j+1]
                    
                    if tab[i]:
                        break
            
            return tab[0]
        
        return dfs()


