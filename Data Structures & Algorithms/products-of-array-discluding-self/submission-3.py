class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        count = 0
        ans = [0]*len(nums)

        for i in range(len(nums)):
            if nums[i] == 0:
                count += 1
                if count >=2:
                    return ans
                continue
            product *= nums[i]

        for i in range(len(nums)):
            if count == 1 and nums[i] == 0:
                ans[i] = product
                return ans
            elif count == 1:
                continue
            else:
                ans[i] = product//nums[i]
        return ans