class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        prevSmaller = [-1]*len(heights)
        stack = []
        for i in range(len(heights)):
            while len(stack) > 0 and heights[i] <= heights[stack[-1]]:
                stack.pop()
            if len(stack) == 0:
                prevSmaller[i] = -1
            else:
                prevSmaller[i] = stack[-1]
            stack.append(i)
        nextSmaller = [0]*len(heights)
        stack = []
        for i in range(len(heights)-1,-1,-1):
            while len(stack) > 0 and heights[i] <= heights[stack[-1]]:
                stack.pop()
            if len(stack) == 0:
                nextSmaller[i] = len(heights)
            else:
                nextSmaller[i] = stack[-1]
            stack.append(i)
        ans = 0
        for i in range(len(heights)):
            area = (nextSmaller[i] - prevSmaller[i] - 1)*heights[i]
            ans = max(ans,area)
        return ans