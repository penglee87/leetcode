#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''

28. 实现strStr()
题目描述提示帮助提交记录社区讨论阅读解答
实现 strStr() 函数。

给定一个 haystack 字符串和一个 needle 字符串，在 haystack 字符串中找出 needle 字符串出现的第一个位置 (从0开始)。如果不存在，则返回  -1。

示例 1:

输入: haystack = "hello", needle = "ll"
输出: 2
示例 2:

输入: haystack = "aaaaa", needle = "bba"
输出: -1
说明:

当 needle 是空字符串时，我们应当返回什么值呢？这是一个在面试中很好的问题。

对于本题而言，当 needle 是空字符串时我们应当返回 0 。这与C语言的 strstr() 以及 Java的 indexOf() 定义相符。

'''

class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        size1 = len(haystack)
        size2 = len(needle)
        if size2 == 0:
            return 0
        if size1 < size2:
            return -1
        i = 0
        while i < size1:
            if size1 - i < size2:
                return -1
            if haystack[i] == needle[0]:
                j = 1
                while j < size2:
                    if haystack[i + j] != needle[j]:
                        break
                    j += 1
                if j == size2:
                    return i
            i += 1
        return -1


if __name__ == '__main__':
    haystack = "aaaabba"
    needle = "bba"
    sol = Solution()
    r = sol.strStr(haystack,needle)
    print(r)
