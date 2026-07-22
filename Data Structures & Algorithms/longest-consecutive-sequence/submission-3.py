class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        ans = 0
        for i in range(len(nums)):
            if nums[i] - 1 not in s:
                j = nums[i]
                ls = 0
                while j in s:
                    ls += 1
                    j += 1
                ans = max(ls,ans)

        return ans
                
            