#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
给定一个包含 n 个整数的数组 nums 和一个目标值 target，判断 nums 中是否存在四个元素 a，b，c 和 d ，使得 a + b + c + d 的值与 target 相等？找出所有满足条件且不重复的四元组。

注意：

答案中不可以包含重复的四元组。

示例：

给定数组 nums = [1, 0, -1, 0, -2, 2]，和 target = 0。

满足要求的四元组集合为：
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]

题目思路：
这道题做法和3Sum的一样，先排好序。固定两个数，剩下的两个数夹逼定理找出。总的时间复杂度(O(n^3))。
其中可以做一些简单的优化，比如夹逼的时候，如果最小两个数之和大于target - 前两个数，或者最大的两个数之和小于target - 前两个数直接跳出。

'''

class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        size = len(nums)
        ans = []
        if size < 4:
            return ans
        nums.sort()
        i = 0
        while i < size - 3:
            j = i + 1
            while j < size - 2:
                tmp = target - nums[i]- nums[j]
                k = j + 1
                t = size - 1
                while k < t:
                    if nums[k] + nums[k + 1] > tmp or nums[t] + nums[t-1]< tmp:
                        break
                    if nums[k] + nums[t] < tmp:
                        k += 1
                    elif nums[k] + nums[t] > tmp:
                        t -= 1
                    else:
                        ans.append([nums[i],nums[j],nums[k],nums[t]])
                        k += 1
                        t -= 1
                        while k < t:
                            if nums[k] == nums[k -1]:
                                k += 1
                            if nums[t] == nums[t+1]:
                                t -= 1
                            if nums[k] != nums[k - 1] and nums[t] != nums[t+1]:
                                break
                j += 1
                while j < size - 2:
                    if nums[j] != nums[j - 1]:
                        break
                    j += 1
            i += 1
            while i < size - 3:
                if nums[i] != nums[i - 1]:
                    break
                i += 1
        return ans


if __name__ == '__main__':
    s = [1, 0, -1, 0, -2, 2]
    t = 0
    sol = Solution()
    r = sol.fourSum(s,t)
    print(r)
