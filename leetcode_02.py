#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
两数相加
给定两个非空链表来代表两个非负整数，位数按照逆序方式存储，它们的每个节点只存储单个数字。将这两数相加会返回一个新的链表。

你可以假设除了数字 0 之外，这两个数字都不会以零开头。

示例：

输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
输出：7 -> 0 -> 8
原因：342 + 465 = 807

题目思路：
不难发现，其实题目就是要我们模拟加法的实现。那么，我们就直接从低位（链条第一位）开始，同位相加，满10就往高位+1。
'''
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class ListNode_handle(object):
    def __init__(self):  
        self.cur_node = None

    def add(self, data):
        #add a new node pointed to previous node  
        node = ListNode(0)
        node.val = data  
        node.next = self.cur_node
        self.cur_node = node
        return node  
  
    def print_ListNode(self, node):
        while node:  
            print ('\nnode: ', node, ' value: ', node.val, ' next: ', node.next)
            node = node.next  

    def _reverse(self, nodelist):
        list = []
        while nodelist:
            list.append(nodelist.val)
            nodelist = nodelist.next
        result = ListNode()
        result_handle = ListNode_handle()
        for i in list:  
            result = result_handle.add(i)
        return result  

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        ans = ListNode(0)
        tmp = ans
        tmpsum = 0
        while True:
            if l1 != None:
                tmpsum += l1.val
                l1 = l1.next
            if l2 != None:
                tmpsum += l2.val
                l2 = l2.next
            tmp.val = tmpsum % 10
            tmpsum //= 10
            if l1 == None and l2 == None and tmpsum == 0:
                break
            tmp.next = ListNode(0)
            tmp = tmp.next
        return ans


if __name__ == '__main__':
    l1_list = [2 , 4 , 3]
    l2_list = [5 , 6 , 4]
    l1 = ListNode(0)
    l2 = ListNode(0)
    ListNode_1 = ListNode_handle()
    ListNode_2 = ListNode_handle()
    for i in l1_list:
        l1 = ListNode_1.add(i)
    for i in l2_list:
        l2 = ListNode_2.add(i)
    sol = Solution()
    r = sol.addTwoNumbers(l1,l2)
    print(r)
    ListNode_r = ListNode_handle()
    ListNode_r.print_ListNode(r)