class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        ans = []
        def backtrack(target,i):
            if i == len(nums):
                return
            if target == 0:
                res.append(ans[:])
                return
            if target < 0:
                return
            ans.append(nums[i])
            backtrack(target-nums[i],i)
            ans.pop()
            backtrack(target,i+1)
        backtrack(target,0)
        return res

