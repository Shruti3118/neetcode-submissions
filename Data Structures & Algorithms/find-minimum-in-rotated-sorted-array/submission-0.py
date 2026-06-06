class Solution:
    def findMin(self, nums: List[int]) -> int:
        if (len(nums)==1):
            return nums[0]
        low = 0
        high = len(nums) - 1
        minL = nums[0]
        while low<=high:
            mid = (low+high)//2
            if nums[low] <= nums[mid]:
                minL = min(nums[low],minL)
                low = mid + 1
            else:
                minL = min(nums[mid],minL)
                high = mid - 1
        return minL

        