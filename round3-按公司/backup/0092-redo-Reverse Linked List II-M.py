'''
92. Reverse Linked List II

Given the head of a singly linked list and two integers left and right where left <= right, reverse the nodes of the list from position left to position right, and return the reversed list.
'''

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        pre = tail = dummy
        i = j = 0
        while i < left - 1:
            pre = pre.next
            i += 1
        while j < right + 1:
            tail = tail.next
            j += 1
        cur = pre.next
        nex = cur.next
        #print(pre.val, tail.val)
        i = 0
        while i < right - left + 1:
            #print(cur.val, nex.val, tail.val)
            cur.next = tail
            tail = cur
            cur = nex
            if cur:
                nex = cur.next
            i += 1
        pre.next = tail
        return dummy.next

'''
这个方法不错，适合知道步数的
注意pre的步长是left-1
'''
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        pre = dummy
        for _ in range(left - 1):
            pre = pre.next
        cur = pre.next
        #print(pre.val, cur.val)
        for _ in range(right-left):
            p = cur.next
            cur.next = cur.next.next
            p.next = pre.next
            pre.next = p
        return dummy.next

'''
不知道长度的方法
'''

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        pre_node =  dummy
        for _ in range(left - 1):
            pre_node = pre_node.next
        right_node = pre_node
        for _ in range(right - left + 1):
            right_node = right_node.next
        print(pre_node.val, right_node.val)
        left_node, tail_node = pre_node.next, right_node.next
        pre_node.next, right_node.next = None, None
        self.reverse(left_node)
        pre_node.next = right_node
        left_node.next = tail_node
        return dummy.next
        
    def reverse(self, head):
        pre, cur = None, head
        while cur:
            next_ = cur.next
            cur.next = pre
            pre = cur
            cur = next_
        