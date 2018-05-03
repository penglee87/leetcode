#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
给定一个 32 位有符号整数，将整数中的数字进行反转。

示例 1:

输入: 123
输出: 321
 示例 2:

输入: -123
输出: -321
示例 3:

输入: 120
输出: 21
注意:

假设我们的环境只能存储 32 位有符号整数，其数值范围是 [−231,  231 − 1]。根据这个假设，如果反转后的整数溢出，则返回 0。
'''

class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        ans = 0
        x1 = abs(x)
        while x1>0:
            ans = ans*10 + x1%10
            x1 = x1//10
            
        if ans > pow(2,31)-1:
            return 0
        elif x>0:
            return(ans)
        else:
            return(-ans)


if __name__ == '__main__':
    s = -123
    sol = Solution()
    r = sol.reverse(s)
    print(r)
