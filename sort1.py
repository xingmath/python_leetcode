# -*- coding: utf-8 -*-
"""
Created on Sat Sep 29 10:19:41 2018

@author: www
"""

#1->2->3->4转换成2->1->4->3.
class ListNode(object):
    def __init__(self,x):
        self.val = x
        self.next = None
        
class solution(object):
    def change(self,aa):
        if aa is None or aa.next is None:
            return aa
        else :
            ans = aa.next
            print(ans.val)
            aa.next = self.change(ans.next)
            print(aa.next.val)
            ans.next = aa
            return ans

aa=ListNode(1)
print(aa.val,aa.next)

aa.next=ListNode(2)
print(aa.val,aa.next.val)

aa.next.next=ListNode(3)
print(aa.val,aa.next.val)

aa.next.next.next=ListNode(4)
print(aa.val,aa.next.val,aa.next.next.val,aa.next.next.next.val)

s=solution()
res=s.change(aa)



class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # @param a ListNode
    # @return a ListNode
    def swapPairs(self, head):
        if head != None and head.next != None:
            next = head.next
            head.next = self.swapPairs(next.next)
            next.next = head
            return next
        return head

    