class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            return self.medianSortedArrays(nums2,nums1)
        else:
            return self.medianSortedArrays(nums1,nums2)
    def medianSortedArrays(self,nums1,nums2):
        n1 = len(nums1)
        n2 = len(nums2)
        low = 0
        high = n1
        while low <= high:
            i1 = (low+high)//2
            i2 = (n1+n2+1)//2 - i1
            min1 = float('inf') if i1 == n1 else nums1[i1]
            max1 = float('-inf') if i1 == 0 else nums1[i1-1]
            min2 = float('inf') if i2 == n2 else nums2[i2]
            max2 = float('-inf') if i2 == 0 else nums2[i2-1]
            if max1 <= min2 and max2 <=min1:
                if (n1+n2)%2 == 0:
                    return (max(max1,max2)+min(min1,min2))/2
                else:
                    return float(max(max1,max2))
            elif max1 > min2:
                high = i1-1
            else:
                low = i1+1


