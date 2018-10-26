#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''

239. 滑动窗口最大值
题目描述提示帮助提交记录社区讨论阅读解答
给定一个数组 nums，有一个大小为 k 的滑动窗口从数组的最左侧移动到数组的最右侧。你只可以看到在滑动窗口 k 内的数字。滑动窗口每次只向右移动一位。

返回滑动窗口最大值。

示例:

输入: nums = [1,3,-1,-3,5,3,6,7], 和 k = 3
输出: [3,3,5,5,6,7] 
解释: 

  滑动窗口的位置                最大值
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
注意：

你可以假设 k 总是有效的，1 ≤ k ≤ 输入数组的大小，且输入数组不为空。

进阶：

你能在线性时间复杂度内解决此题吗？

'''

class Solution:
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if not nums:
            return []
        window,res=[],[]  #window存放下标
        for i,x in enumerate(nums):
            if i>=k and window[0]<=i-k:  #第一个下标比i-k还小
                window.pop(0)
            while window and nums[window[-1]]<=x:
                window.pop()
            window.append(i)
            if i>=k-1:
                res.append(nums[window[0]])
        return res
        
        
        
if __name__ == '__main__':
    nums = [1,3,-1,-3,5,3,6,7]
    k = 3
    sol = Solution()
    r = sol.maxSlidingWindow(nums,3)
    print(r)
