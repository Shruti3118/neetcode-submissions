class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        r = 0
        hm = {}
        res = 0
        freq = 0
        while r < len(s):
            hm[s[r]] = hm.get(s[r],0)+1
            freq = max(hm[s[r]],freq)
            while r - l + 1 - freq > k:
                hm[s[l]] -= 1
                l += 1
            res = max(r-l+1,res)
            r += 1
        return res
            