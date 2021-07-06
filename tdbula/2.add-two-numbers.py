#
# @lc app=leetcode id=2 lang=python3
#
# [2] Add Two Numbers
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        res = temp = ListNode()

        carry = 0
        while l1 and l2:
            tot = l1.val + l2.val + carry
            carry, val = divmod(tot, 10)
            temp.next = ListNode(val)
            temp = temp.next
            l1 = l1.next
            l2 = l2. next

        
        while l1:
            tot = l1.val + carry
            carry, val = divmod(tot, 10)
            temp.next = ListNode(val)
            temp = temp.next
            l1 = l1.next 

        while l2:
            tot = l2.val + carry
            carry, val = divmod(tot, 10)
            temp.next = ListNode(val)
            temp = temp.next
            l2 = l2.next 

        if carry:
            temp.next = ListNode(carry)
            
        return res.next
# @lc code=end

