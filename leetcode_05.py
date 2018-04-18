#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
最长回文子串
给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 长度最长为1000。

示例:

输入: "babad"

输出: "bab"

注意: "aba"也是有效答案
 

示例:

输入: "cbbd"

输出: "bb"
'''

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        size = len(s)
        if size == 1:
            return s
        if size == 2:
            if s[0] == s[1]:
                return s
            return s[0]
        maxp = 1
        ans = s[0]
        i = 0
        while i < size:
            j = i + 1
            # j 用于保存后面连续相同字符串截止位置
            while j < size:
                if s[i] == s[j]:
                    j += 1
                else:
                    break
            k = 0
            # 判断是否越界
            while i - k - 1 >= 0 and j + k<= size - 1:
                # 从i开始向前k位与从j开始向后k位进行对比
                if s[i- k - 1] != s[j + k]:
                    break
                k += 1
            if j - i + 2*k > maxp:
                maxp = j- i + 2*k
                ans = s[i - k:j + k]
            if j + k == size - 1:
                break
            i = j
        return ans

        

if __name__ == '__main__':
    s = 'abcbcdbb'
    sol = Solution()
    r = sol.longestPalindrome(s)
    print(r)
