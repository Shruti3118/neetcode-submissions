class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s1 = [0]*26
        t1 = [0]*26
        for i in range(len(s)):
            val = ord(s[i])-ord('a')
            s1[val] += 1
            val = ord(t[i])-ord('a')
            t1[val] += 1
        return s1 == t1
        


        