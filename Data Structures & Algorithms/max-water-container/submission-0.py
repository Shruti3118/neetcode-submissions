class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0
        j = len(heights) - 1
        ans = 0
        while i < j:
            currArea = (j - i)*min(heights[i],heights[j])
            if heights[j] > heights[i]:
                i += 1
            else:
                j -= 1
            ans = max(currArea,ans)
        return ans 

        