#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
无重复字符的最长子串
给定一个字符串，找出不含有重复字符的 最长子串 的长度。

示例：

给定 "abcabcbb" ，没有重复字符的最长子串是 "abc" ，那么长度就是3。

给定 "bbbbb" ，最长的子串就是 "b" ，长度是1。

给定 "pwwkew" ，最长子串是 "wke" ，长度是3。请注意答案必须是一个子串，"pwke" 是 子序列 而不是子串。

题目思路：
首先，我们可以想到的方法就是每个字符为起点，找到对应的最长不重复子字符串长度，最后进行比较得到最长的不重复子字符串长度。
这个方法的时间复杂度为（O（n^2）)。如果用这个方法，那么很容易就会TLE。

那么我们回想一下题目例子我们找无重复子字符串的过程。我们从第二个a开始找的时候，找到了倒数第二个b，发现b已经出现过了，
这时候，我们再从第二个b开始找，那么得到的无重复子字符串必定比从a开始找要短，那么我们就不需要再从b开始找，而是从c开始找。
也就是说，当我们发现这个字符在前面的无重复子字符串出现的位置后一位开始找。
如此我们可以节省很多时间，并且我们只需要从头找一次就可以得到答案。时间复杂度为（O（nlogn））。
'''

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        lls = 1  #记录不重复字符串的长度
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1
        i = 1
        curbegin = 0  #记录本次不重复字符串的开始位置
        while i < len(s):
            cur = s.find(s[i],curbegin,i)
            if cur != -1:  #判断字符串s[i]是否在之前出现过（如果之前已出现）
                if i - curbegin > lls:  #i - curbegin,本次不重复字符串的长度
                    lls = i - curbegin
                    maxstr = s[curbegin:curbegin+lls]
                curbegin = cur + 1
            i += 1
        if s.find(s[len(s) - 1],curbegin,len(s) - 1) == -1:  #遍历最后一个字符
            if len(s) - curbegin > lls:
                lls = len(s) - curbegin
                maxstr = s[-lls:]
                return(lls,maxstr)
        return lls,maxstr


if __name__ == '__main__':
    s = 'abcdbcdbbcde'
    sol = Solution()
    r = sol.lengthOfLongestSubstring(s)
    print(r)
