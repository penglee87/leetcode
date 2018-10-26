#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''

30. 与所有单词相关联的字串
题目描述提示帮助提交记录社区讨论阅读解答
给定一个字符串 s 和一些长度相同的单词 words。在 s 中找出可以恰好串联 words 中所有单词的子串的起始位置。

注意子串要与 words 中的单词完全匹配，中间不能有其他字符，但不需要考虑 words 中单词串联的顺序。

示例 1:

输入:
  s = "barfoothefoobarman",
  words = ["foo","bar"]
输出: [0,9]
解释: 从索引 0 和 9 开始的子串分别是 "barfoor" 和 "foobar" 。
输出的顺序不重要, [9,0] 也是有效答案。
示例 2:

输入:
  s = "wordgoodstudentgoodword",
  words = ["word","student"]
输出: []


题目思路：

由于给定的words的长度是相同的，题目难度就降低了很多。题目难度就在于判断一个字符串是否仅由words构成。
这里，我们可以构造一个字典，key对应的是words出现的次数。将字符串截成n个words长度的字符串，如果这些字符串出现在字典里面，字典对应的次数-1.如果所有字典为0则满足。

'''

class Solution(object):
    def match(self,s,dict,size):
        i = 0
        while i <= len(s)- size:
            tmp = s[i:i + size]
            if tmp in dict and dict[tmp] != 0:
                dict[tmp] -= 1
            else:
                return False
            i += size
        return True
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        sizew = len(words)
        if sizew == 0:
            return []
        d = {}
        ans = []
        for i in words:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        j = 0
        ss = len(s); sw = len(words[0])
        while j <= ss - sizew * sw:
            tmpd = d.copy()
            if self.match(s[j:j + sizew * sw],tmpd,sw):
                ans.append(j)
            j += 1
        return ans
        
        
        
if __name__ == '__main__':
    s = 'swordstudentgoodstudentgoodstudword'
    words = ["word","stud","entg"]
    sol = Solution()
    r = sol.findSubstring(s,words)
    print(r)
