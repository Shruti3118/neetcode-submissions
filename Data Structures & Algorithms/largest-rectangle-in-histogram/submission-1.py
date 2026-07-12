class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = []
        for i in range(len(heights)):
            while len(stack) > 0 and heights[i] <= heights[stack[-1]]:
                val = stack.pop()
                currArea = (i - stack[-1] - 1)*heights[val] if len(stack) > 0 else i*heights[val]
                maxArea = max(maxArea,currArea)
            stack.append(i)
        while len(stack) > 0:
            val = stack.pop()
            currArea = (len(heights) - stack[-1] - 1)*heights[val] if len(stack) > 0 else len(heights)*heights[val]
            maxArea = max(currArea,maxArea)
        return maxArea