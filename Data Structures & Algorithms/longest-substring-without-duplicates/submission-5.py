class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 0
        prev = [-1]*256
        ans = 0
        while r < len(s):
            l = max(prev[ord(s[r])]+1,l)
            ans = max(r-l+1,ans)
            print(ans)
            prev[ord(s[r])] = r
            r += 1
        return ans
            

            
            


