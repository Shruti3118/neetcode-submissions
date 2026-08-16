class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        res = []
        ans = []

        hm = {}
        hm[2] = list("abc")
        hm[3] = list("def")
        hm[4] = list("ghi")
        hm[5] = list("jkl")
        hm[6] = list("mno")
        hm[7] = list("pqrs")
        hm[8] = list("tuv")
        hm[9] = list("wxyz")

        def dfs(i):
            if i == len(digits):
                res.append("".join(ans[:]))
                return

            for ch in hm[int(digits[i])]:
                ans.append(ch)
                dfs(i+1)
                ans.pop()
        
        dfs(0)
        return res