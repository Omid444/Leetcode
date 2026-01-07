class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        main_list = nums1 + nums2
        sorted_numbs = sorted(main_list)
        lenght = len(sorted_numbs)
        mid = lenght // 2
        odd_even = lenght % 2
        print(odd_even)
        if odd_even == 0:

            median = (sorted_numbs[mid-1] + sorted_numbs[mid]) / 2.0
            return median

        else:
            median = sorted_numbs[mid]
            return median




s = Solution()
print(s.findMedianSortedArrays([1,2], [3,4]))