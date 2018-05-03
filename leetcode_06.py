#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
将字符串 "PAYPALISHIRING" 以Z字形排列成给定的行数：

P   A   H   N
A P L S I I G
Y   I   R
之后从左往右，逐行读取字符："PAHNAPLSIIGYIR"

实现一个将字符串进行指定行数变换的函数:

string convert(string s, int numRows);
示例 1:

输入: s = "PAYPALISHIRING", numRows = 3
输出: "PAHNAPLSIIGYIR"
示例 2:

输入: s = "PAYPALISHIRING", numRows = 4
输出: "PINALSIGYAHRPI"
解释:

P     I    N
A   L S  I G
Y A   H R
P     I


题目思路：
这题只是简单的字符串处理。首先，我们可以对Z形字符串进行简单优化一下，将Z中的“折”合起来。比如：“ABCDEFGHIJKL”，4

A  G  M
B FH LN
CE IK O
D  J  P
优化后：

A G M
BFHLN
CEIKO
D J P
不难发现，得到的结果不变，而列表的列数减少了，且每2*numRows-2为一个循环
'''

class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        size = len(s)
        if size <= numRows or numRows == 1:
            return s
        ans = ''
        i = 0
        while i < numRows:
            j = i
            if i == 0 or i == numRows - 1:
                while j < size:
                    ans += s[j]
                    j += 2*numRows - 2
                    #if 2 * numRows - 2 == 0:
                    #    break
            else:  #i属于中间行
                while j < size:
                    ans += s[j]
                    j += 2*(numRows - i) - 2  #跳转至Z字形向上返回到此行的位置
                    if j >= size:
                        break
                    ans += s[j]
                    j += 2*i  #Z字形下一次向下的位置（完成一次循环）
            i += 1
        return ans


if __name__ == '__main__':
    s = 'ABCDEFGHIJKLMNOPQRST'
    print(len(s))
    numRows = 1
    sol = Solution()
    r = sol.convert(s,numRows)
    print(len(r),r)
