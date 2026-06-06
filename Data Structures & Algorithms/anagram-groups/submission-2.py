class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hm = {}
        for i in range(len(strs)):
            charArray = [0]*26
            for j in range(len(strs[i])):
                charArray[ord(strs[i][j]) - ord('a')]+=1
            if tuple(charArray) in hm:
                hm[tuple(charArray)].append(strs[i])
            else:
                hm[tuple(charArray)] = [strs[i]]
        ans = []
        for elem in hm:
            ans.append(hm[elem])
        return ans





