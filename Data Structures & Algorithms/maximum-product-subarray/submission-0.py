class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        def rec_tab():
            currMax = 1
            currMin = 1
            res = nums[0]

            for i in range(len(nums)):
                val = currMax*nums[i]

                currMax = max(nums[i], val, nums[i]*currMin)
                currMin = min(nums[i], val, nums[i]*currMin)

                res = max(res,currMax)

            return res
        
        return rec_tab()

# [-8, 4, -3, -5]