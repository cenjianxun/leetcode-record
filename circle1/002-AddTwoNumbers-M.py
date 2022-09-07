'''
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
'''
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
        
'''
210510 
这题卡在链表。链表每一个node都需要现场制作，然后再串起来。

210824
会了会了
'''

class Solution:
    def addTwoNumbers(self, l1, l2):
        l = ListNode(0)
        curNode = l
        flag = 0
        while l1 or l2:
            num = flag
            if l1:
                num = num + l1.val
                l1 = l1.next
            if l2:
                num = num + l2.val
                l2 = l2.next
            curNode.next = ListNode(num%10)
            flag = num//10
            curNode = curNode.next

        if flag:
            curNode.next = ListNode(flag)
        return l.next
        