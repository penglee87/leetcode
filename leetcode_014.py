#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''

编写一个函数来查找字符串数组中的最长公共前缀。

如果不存在公共前缀，返回空字符串 ""。

示例 1:

输入: ["flower","flow","flight"]
输出: "fl"
示例 2:

输入: ["dog","racecar","car"]
输出: ""
解释: 输入不存在公共前缀。
说明:

所有输入只包含小写字母 a-z 。

题目思路：
从字符串头部开始计算，初始化公共前缀子字符串是strs[0]，
公共子字符串每和下一个字符串得到一个新的最新公共前缀子字符串，直到公共前缀子字符串是空或者比较到了最后一个字符串。

'''

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        size = len(strs)
        if size == 0:
            return ''
        if size == 1:
            return strs[0]
        ans = strs[0]
        for i in range(1, size):
            j = 0
            minlen = min(len(ans),len(strs[i]))
            #print(minlen)
            while j < minlen:
                if ans[j] != strs[i][j]:
                    break
                j += 1
            if j == 0:
                return ''
            ans = ans[:j]
            i += 1
        return ans




if __name__ == '__main__':
    s = ['abc','abb']
    sol = Solution()
    r = sol.longestCommonPrefix(s)
    print(r)
