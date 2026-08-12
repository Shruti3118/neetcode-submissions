class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        def backtrack(ans,i):
            if i == len(nums):
                res.append(ans[:])
                return
            
            ans.append(nums[i])
            backtrack(ans,i+1)

            while i < len(nums) - 1 and nums[i] == nums[i+1]:
                i += 1
            
            ans.pop()
            backtrack(ans,i+1)
        backtrack([],0)
        return res
