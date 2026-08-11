class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        ans = []
        def backtrack(visited):
            if len(ans) == len(nums):
                res.append(ans[:])
            
            for i in range(len(nums)):
                if visited[i] == False:
                    ans.append(nums[i])
                    visited[i] = True

                    backtrack(visited)

                    visited[i] = False
                    ans.pop()
        backtrack([False]*len(nums))
        return res
        
