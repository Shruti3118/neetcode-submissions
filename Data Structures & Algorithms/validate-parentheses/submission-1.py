class Solution:
    def isValid(self, s: str) -> bool:
        hm = {}
        hm['('] = ')'
        hm['{'] = '}'
        hm['['] = ']'
        paran = []
        for i in range(len(s)):
            if s[i] in hm:
                paran.append(hm[s[i]])
            else:
                if len(paran) < 1:
                    return False
                if s[i] != paran[-1]:
                    return False
                else:
                    paran.pop()
        if len(paran) > 0:
            return False
        return True
                
        