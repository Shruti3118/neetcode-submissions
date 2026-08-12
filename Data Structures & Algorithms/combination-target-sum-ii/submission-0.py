class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        def backtrack(target,ans,i):
            if target == 0:
                res.append(ans[:])
                return
            if i == len(candidates):
                return
            if target < 0:
                return
            
            ans.append(candidates[i])
            backtrack(target - candidates[i],ans,i+1)
            while i < len(candidates) - 1 and candidates[i] == candidates[i+1]:
                i += 1

            ans.pop()
            backtrack(target,ans,i+1)
        
        backtrack(target,[],0)
        return res

            
            


        