#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''

给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。

有效字符串需满足：

左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
注意空字符串可被认为是有效字符串。

示例 1:

输入: "()"
输出: true
示例 2:

输入: "()[]{}"
输出: true
示例 3:

输入: "(]"
输出: false
示例 4:

输入: "([)]"
输出: false
示例 5:

输入: "{[]}"
输出: true

题目思路：
当我们面对一串括号的字符串，首先我们人工的做法是先把确定可以配对的，也就是括号间没有其他字符的先配对，然后去掉，剩下的继续用这种方法去做。
要用程序来实现这个过程，我们可以利用堆栈来做，也就是C++里面的stack。如果遇到左括号，我们就将括号push到一个stack里面，如果遇到右括号，那么将stack的队尾pop出，比较是否可以配对，
如果可以，继续，如果不可以，返回False。在python里面list也可以当作stack来用。只不过push变成了append。

'''

class Solution(object):
    def match(self,s1,s2):
        if s1 == '(' and s2 ==')':
            return True
        if s1 == '[' and s2 ==']':
            return True
        if s1 == '{' and s2 =='}':
            return True
        return False
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        ans = []
        for i in s:
            if i == '(' or i == '{' or i == '[':  #加入正括号
                ans.append(i)
            if i == ')' or i == ']' or i == '}':  #碰到反括号，则与已加入的正括号pop出来的最后一个进行对比
                if len(ans) == 0:
                    return False
                tmp = ans.pop()
                if not self.match(tmp,i):
                    return False
        if len(ans) == 0:  #若最后每一个pop出正括号都能匹配
            return True
        return False


if __name__ == '__main__':
    s = '{1[]}'
    sol = Solution()
    r = sol.isValid(s)
    print(r)
