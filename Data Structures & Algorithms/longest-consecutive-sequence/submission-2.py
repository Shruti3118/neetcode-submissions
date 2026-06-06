class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        res = 0
        for elem in nums:
            i = elem - 1
            if i not in s:
                i = elem + 1
                curr = 1
                while i in s:
                    curr+=1
                    i+=1
                res = max(curr,res)
        return res