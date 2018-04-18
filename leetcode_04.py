#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
两个排序数组的中位数

有两个大小为 m 和 n 的排序数组 nums1 和 nums2 。

请找出两个排序数组的中位数并且总的运行时间复杂度为 O(log (m+n)) 。

示例 1:

nums1 = [1, 3]
nums2 = [2]

中位数是 2.0
 

示例 2:

nums1 = [1, 2]
nums2 = [3, 4]

中位数是 (2 + 3)/2 = 2.5
'''

class Solution(object):
    def getMedian(self,nums):
        size = len(nums)
        if size == 0:
            return [0,0]
        if size % 2 == 1:
            return [nums[size // 2],size // 2]
        return [(float(nums[size // 2 - 1] + nums[size // 2])) / 2,size // 2]
        
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        size1 = len(nums1)
        size2 = len(nums2)
        if size1 < size2:
            return self.findMedianSortedArrays(nums2,nums1)
        m1 = self.getMedian(nums1)
        m2 = self.getMedian(nums2)
        if size2 == 0:
            return m1[0]
        if size2 == 1:
            if size1 == 1:
                return (float(nums1[0] + nums2[0])) / 2
            if size1 % 2 == 0:
                if nums2[0] < nums1[size1 //2 - 1]:
                    return nums1[size1 // 2 - 1]
                if nums2[0] > nums1[size1 // 2 ]:
                    return nums1[size1 // 2]
                else:
                    return nums2[0]
            else:
                if nums2[0] < nums1[size1 // 2 - 1]:
                    return (float(nums1[size1 // 2 - 1] + nums1[size1 // 2])) / 2
                if nums2[0] > nums1[size1 // 2 + 1]:
                    return (float(nums1[size1 // 2] + nums1[size1 // 2 + 1])) / 2
                else:
                    return (float(nums2[0] + nums1[size1 // 2])) / 2
        if size2 % 2 == 0:
            if size1 % 2 == 0:
                if nums2[size2 // 2 - 1] < nums1[size1 //2 - 1] and nums2[size2 // 2] > nums1[size1 // 2]:
                    return m1[0]
                if nums1[size1 // 2 - 1] < nums2[size2 // 2 - 1] and nums1[size1 // 2] > nums2[size2 // 2]:
                    return m2[0]
        if m1[0] < m2[0]:
            return self.findMedianSortedArrays(nums1[m2[1]:],nums2[:size2 - m2[1]])
        if m1[0] > m2[0]:
            return self.findMedianSortedArrays(nums1[:size1 - m2[1]],nums2[m2[1]:])
        else:
            return m1[0]


if __name__ == '__main__':
    nums1 = [1,3,5]
    nums2 = [2,7,8]
    sol = Solution()
    r = sol.findMedianSortedArrays(nums1, nums2)
    print(r)
