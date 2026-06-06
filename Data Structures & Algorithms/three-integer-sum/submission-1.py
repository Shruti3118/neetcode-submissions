class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = set()
        for i in range(len(nums)-2):
            j = i+1
            k = len(nums)-1
            while j < k:
                if nums[j]+nums[k] == 0 - nums[i]:
                    ans.add((nums[i],nums[j],nums[k]))
                    j += 1
                    k -= 1
                elif nums[i]+nums[j]+nums[k] < 0:
                    j += 1
                else:
                    k -=1
        return [list(x) for x in ans]
        