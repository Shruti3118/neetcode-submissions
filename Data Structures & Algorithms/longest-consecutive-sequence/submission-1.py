class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set()
        res = 0
        for elem in nums:
            s.add(elem)
        for elem in nums:
            curr = 1
            i = elem - 1
            while i in s:
                curr+=1
                i -= 1
            res = max(res,curr)
        return res