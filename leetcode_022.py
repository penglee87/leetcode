#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''

给出 n 代表生成括号的对数，请你写出一个函数，使其能够生成所有可能的并且有效的括号组合。

例如，给出 n = 3，生成结果为：

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]

题目思路：
①不难发现，n为0的时候输出是空，而n = 1的时候，输出“（）”
②当n > 1的时候，要使得整个括号字符串可以配对，那么与第一个配对的右括号把n - 1对括号分成了一个 i （0 <= i < n）对已配对的括号和 n - 1 - i对已配对的括号。
那么把所有的右括号划分的情况全部列出来就可以了。由于这里的时间复杂度比较复杂，就不作分析了。

根据上述可以得到：
f(n) = ∑(   '(' + f(i) +')' + f(n - 1 - i)   )

'''

class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ans = []
        if n == 0:
            return ans
        if n == 1:
            return ['()']
        i = 0
        while i < n:
            tmp1 = self.generateParenthesis(i)
            print('tmp1',tmp1,'n',n,'i',i,'ans',ans)
            tmp2 = self.generateParenthesis(n - 1 - i)  #i=0时，传入参数为4-1-0=3，tmp1再次执行,此时i=0,tmp2再次执行时传入参数为3-1-0 (n不是固定不变的)
            print('tmp2',tmp2,'n',n,'i',i,'ans',ans)
            for j in tmp1:
                print('tmptmp1',tmp1)
                for k in tmp2:
                    print('tmptmp2',tmp2)
                    ans.append('(' + j + ')' + k)
                if len(tmp2) == 0:
                    ans.append('(' + j + ')')
            if len(tmp1) == 0:
                for k in tmp2:
                    ans.append('()' + k)
            i += 1
        return ans


if __name__ == '__main__':
    s = 4
    sol = Solution()
    r = sol.generateParenthesis(s)
    print(r)
