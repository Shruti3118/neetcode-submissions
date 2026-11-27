class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        l = 0

        minLen = float('inf')
        sumElems = 0
        
        for r in range(len(nums)):

            sumElems += nums[r]

            while sumElems >= target:

                minLen = min(r - l + 1, minLen)
                sumElems -= nums[l]
                l += 1
        
        if minLen == float('inf'):
            return 0
        
        return minLen


                
            

            