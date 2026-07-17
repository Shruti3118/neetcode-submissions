class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        lmax = height[l]
        r = len(height) - 1
        rmax = height[r]
        ans = 0
        while l < r:
            if height[l] < height[r]:
                l += 1
                lmax = max(lmax,height[l])
                ans += lmax - height[l]
            else:
                r -= 1
                rmax = max(rmax,height[r])
                ans += rmax - height[r]
        return ans

