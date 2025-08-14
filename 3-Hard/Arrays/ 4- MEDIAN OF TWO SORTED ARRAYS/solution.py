class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        merged_array =  nums1 + nums2
        merged_array.sort()
        n= len(merged_array)
        if  n % 2 == 1: 
            median = merged_array[n//2]
            return median 
        else: 
            median = (merged_array[n//2 -1] + merged_array[n//2]) / 2.0
            return median
