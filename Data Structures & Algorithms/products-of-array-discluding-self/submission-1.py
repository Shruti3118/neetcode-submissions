class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        count = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                count += 1
                continue
            if count == 2:
                break
            product *= nums[i]
        ans = [0]*len(nums)
        for i in range(len(nums)):
            if count == 1 and nums[i] == 0:
                ans[i] = product
                return ans
            elif count == 1:
                continue
            elif count >= 2:
                return ans
            else:
                ans[i] = product//nums[i]
        return ans