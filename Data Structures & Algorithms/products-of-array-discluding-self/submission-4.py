class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefProd = [0]*len(nums)
        suffProd = [0]*len(nums)
        prefProd[0] = 1
        for i in range(1,len(nums)):
            prefProd[i] = prefProd[i-1]*nums[i-1]
        suffProd[len(nums)-1] = 1 
        for i in range(len(nums)-2,-1,-1):
            suffProd[i] = suffProd[i+1]*nums[i+1]
        res = []
        for i in range(len(nums)):
            res.append(prefProd[i]*suffProd[i])
        return res
            