class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        ans = []
        def backtrack(i):
            if i == len(s):
                res.append(ans[:])
                return
            
            for j in range(i,len(s)):
                if isPalindrome(s[i:j+1]):
                    ans.append(s[i:j+1])
                    backtrack(j+1)
                    ans.pop()

        def isPalindrome(partition):
            l = 0
            r = len(partition) - 1
            while l < r:
                if partition[l] != partition[r]:
                    return False
                l += 1
                r -= 1
            return True
        
        backtrack(0)
        return res
