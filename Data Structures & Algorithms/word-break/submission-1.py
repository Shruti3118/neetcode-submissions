class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        memo = [-1]*len(s)

        maxLen = 0
        for word in wordDict:
            maxLen = max(maxLen, len(word))

        wordSet = set(wordDict)

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