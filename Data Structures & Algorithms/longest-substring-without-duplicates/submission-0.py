class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = r = 0
        hm = {}
        res = 0
        while r<len(s):
            if s[r] in hm:
                l = max(hm[s[r]] + 1, l)
            hm[s[r]] = r
            res = max(res,r-l+1)
            r += 1
        return res
