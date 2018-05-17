#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''

给定一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？找出所有满足条件且不重复的三元组。

注意：答案中不可以包含重复的三元组。

例如, 给定数组 nums = [-1, 0, 1, 2, -1, -4]，

满足要求的三元组集合为：
[
  [-1, 0, 1],
  [-1, -1, 2]
]

题意分析：
这道题目是输入一个数组nums。找出所有的3个数使得这3个数之和为0.要求1.输出的3个数按小到大排序，2.3个数的组合不重复。
比如输入[-1,0,1,2,-1,-4]，返回的应该是[[-1,0,1],[-1,-1,2]]。

 

题目思路：
如果直接暴力解决，那么时间复杂度是（O（n^3））。这样会TLE。
看到这道题目，我回想了leetcode的第一题。第一题是给出一个数组和一个target，找出数组的两个数使得这两个数等于target。
在第一题中，我提到了”夹逼定理“。这里这个定理就可以用了。首先，我们将输入的数组nums排序。
然后，从头开始取出一个数，nums[i]，在nums[i+1:]中用夹逼定理找出num[j],nums[k](j<k)使得他们的和为0- nums[i]。
然后将[nums[i],nums[j],nums[k]] append到答案数组。
由于会存在多个组合使得nums[i] + nums[j] + nums[k] = 0，所以在比较的时候，
如果nums[j] + nums[k] < 0- nums[i]时候，j += 1；如果nums[j] + nums[k] > 0 - nums[i]时候，k -= 1；
如果nums[j] + nums[k] == 0 - nums[i]的时候，一直j += 1，k -= 1直到nums[j] != nums[j - 1]和nums[k] != nums[k + 1]。
要注意的是，为了避免出现重复的组合，那么i + 的时候也要一直加到nums[i] != nums[i - 1]。

这种方法中，排序的时间复杂度是（O（n*log（n））），夹逼定理的时间复杂度是（O（n）），取数复杂度是（O（n）），
总的时间复杂度是（O（n*log（n）） + O（n）*O（n）） = O（n^2）。所以时间复杂度是O（n^2）。

'''

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        size = len(nums)
        ans = []
        if size <= 2:
            return ans
        nums.sort()
        i = 0
        while i < size -2:
            j = i + 1
            k = size -1
            while j < k:
                if nums[j] + nums[k] + nums[i] < 0:
                    j += 1
                elif nums[j] + nums[k] + nums[i] > 0:
                    k -= 1
                else:
                    ans.append([nums[i],nums[j],nums[k]])
                    j += 1
                    k -= 1
                    while j < k:
                        if nums[j] != nums[j - 1]:
                            break
                        if nums[k] != nums[k + 1]:
                            break
                        j += 1
                        k -= 1
            i += 1
            while i < size - 2:
                if nums[i] != nums[i - 1]:
                    break
                i += 1
        return ans




if __name__ == '__main__':
    s = [-1, 0, 1, 2, -1, -4]
    sol = Solution()
    r = sol.threeSum(s)
    print(r)
