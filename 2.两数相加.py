#
# @lc app=leetcode.cn id=2 lang=python3
#
# [2] 两数相加
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        res = ListNode(0)
        re = res
        carrier = 0
        while l1 or l2:
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0
            r = (x + y + carrier) % 10
            carrier = (x + y + carrier) // 10
            re.next = ListNode(r)
            re = re.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
            
        if carrier > 0:
            re.next = ListNode(1)
        return res.next

# @lc code=end

