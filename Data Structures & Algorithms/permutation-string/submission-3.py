class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        charCount1 = [0]*26
        charCount2 = [0]*26
        for i in range(len(s1)):
            charCount1[ord(s1[i])-ord('a')] += 1
            charCount2[ord(s2[i])-ord('a')] += 1
        matches = 0
        for i in range(26):
            if charCount1[i] == charCount2[i]:
                matches+=1
        l = 0
        r = len(s1) - 1
        while r < len(s2)-1:
            if matches == 26:
                return True
            r += 1
            charCount2[ord(s2[r])-ord('a')] += 1
            if charCount1[ord(s2[r])-ord('a')] == charCount2[ord(s2[r])-ord('a')]:
                matches += 1
            elif charCount1[ord(s2[r])-ord('a')] + 1 == charCount2[ord(s2[r])-ord('a')]:
                matches -= 1
            charCount2[ord(s2[l])-ord('a')] -= 1
            if charCount1[ord(s2[l])-ord('a')] == charCount2[ord(s2[l])-ord('a')]:
                matches += 1
            elif charCount1[ord(s2[l])-ord('a')] - 1 == charCount2[ord(s2[l])-ord('a')]:
                matches -= 1
            l += 1
        return matches == 26    



        
        