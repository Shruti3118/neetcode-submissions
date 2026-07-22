class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        count = 0
        ans = [0]*len(nums)
        for i in range(len(nums)):
            if nums[i] == 0:
                count += 1
                if count > 1:
                    product = 0
                    break
                continue
            product = product*nums[i]
        for i in range(len(nums)):
            if nums[i] == 0:
                ans[i] = product
            elif count == 1:
                ans[i] = 0
            else:
                ans[i] = product//nums[i]
        return ans
