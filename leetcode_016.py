#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''

给定一个包括 n 个整数的数组 nums 和 一个目标值 target。找出 nums 中的三个整数，使得它们的和与 target 最接近。返回这三个数的和。假定每组输入只存在唯一答案。

例如，给定数组 nums = [-1，2，1，-4], 和 target = 1.

与 target 最接近的三个数的和为 2. (-1 + 2 + 1 = 2).

题意分析：
这道题目输入一个数组nums和一个数target，找出数组中三个数，使得他们的和最接近target，返回这三个数的和。


题目思路：

这道题目和上一题3Sum很像，所以也可以用类似的方法去解决这个问题。整个过程分成两步：

①数组排序；这步时间复杂度是（O（nlogn））。

②固定一个数，这步的时间复杂度是（O（n））。

③在剩下的数里面通过“夹逼定理”，找出两个数，使得三个数的和最接近target。这步时间复杂度是（O（n））

总的时间复杂度为（O（nlogn） + O（n）*O(n)） = （O（n^2））。

优化：在第三步的时候通过判断剩下的数中是否最小的两个数相加就大于或者最大两个数就小于target - 第一个数，如果是，则直接判断最小（大）两个数和②中的那个数的和是不是最接近的值。

'''

class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        size = len(nums)
        if size < 3:
            return 0
        nums.sort()
        i = 0 # fix the first index
        ans = nums[0] + nums[1] + nums[size - 1] # ans is used to record the solution
        while i < size - 2:
            tmp = target - nums[i]
            j = i + 1
            k = size - 1
            while j < k:
                if nums[j] + nums[k] == tmp:
                    return target
                if nums[j] + nums[k] > tmp:
                    if nums[j] + nums[j + 1] >= tmp:
                        if nums[j] + nums[j + 1] - tmp < abs(ans - target):
                            ans = nums[i] + nums[j] + nums[j + 1]
                        break
                    tmpans = nums[i] + nums[j] + nums[k]
                    if tmpans - target < abs(ans - target):
                        ans = tmpans
                    k -= 1
                else:
                    if nums[k] + nums[k - 1] <= tmp:
                        if tmp - nums[k] -nums[k - 1] < abs(ans - target):
                            ans = nums[i] + nums[k - 1] + nums[k]
                        break
                    tmpans = nums[i] + nums[j] + nums[k]
                    if target - tmpans < abs(ans - target):
                        ans = tmpans
                    j += 1
            i += 1
            if ans == target:
                return target
        return ans




if __name__ == '__main__':
    s = [-1,2,1,-4]
    t = 1
    sol = Solution()
    r = sol.threeSumClosest(s,t)
    print(r)
