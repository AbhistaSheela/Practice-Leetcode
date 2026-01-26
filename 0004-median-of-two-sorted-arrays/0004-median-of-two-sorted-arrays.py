class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        total=sorted(nums1+nums2)
        length=len(total)
        if length%2==0:
            return (total[length//2 - 1] + total[length//2])/2
        else:
            return total[length//2]