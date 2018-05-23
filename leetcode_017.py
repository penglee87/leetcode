#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''

给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。

给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。
d = {'0':' ','1':'*','2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}；

示例:

输入："23"
输出：["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].

题目思路：

看到这道题目让我想起了向量的笛卡尔乘积。这道题目可以用类似DP的方法去解决。
dp[n] = dp[n -1]X最后一个字符对应的字符串，其中"X"代表内积，也就是说f("123") = f("1") X f("2") X f("3").
首先建立一个字典，d = {'0':' ','1':'*','2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}；
然后对利用笛卡尔乘积做法得到答案。

'''

class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        ans = []
        d = {'0':' ','1':'*','2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
        for element in digits:
            ans = self.addDigit(d[element],ans)  #参数中的ans代表进入的字母组构成的列表
        return ans

    def addDigit(self,digit,ans):
        tmp = []
        for element in digit:
            if len(ans) == 0:
                tmp.append(element)
            for s in ans:
                tmp.append(s + element)  #ans为空是也不会报错，添加空元素，也即不添加
        return tmp


if __name__ == '__main__':
    s = '213'
    sol = Solution()
    r = sol.letterCombinations(s)
    print(r)
