class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        res = []
        def backtrack(opened,closed):            
            if opened == n and closed == n:
                res.append("".join(ans))
                return

            if opened < n:
                ans.append("(")
                backtrack(opened+1,closed)
                ans.pop()

            if closed < opened:
                ans.append(")")
                backtrack(opened,closed+1)
                ans.pop()
        
        backtrack(0,0)
        return res
        
            
                





        