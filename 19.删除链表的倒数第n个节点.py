#
# @lc app=leetcode.cn id=19 lang=python3
#
# [19] 删除链表的倒数第N个节点
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        root = ListNode(0)
        root.next = head
        p1 = root.next
        for i in range(n):
            p1 = p1.next
        p0 = root
        while p1:
            p1 = p1.next
            p0 = p0.next
        p0.next = p0.next.next
        return root.next
        
# @lc code=end

