'''
24. Swap Nodes in Pairs

Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)
'''

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pre = ListNode()
        def swap(p):
            if not p:
                return None
            q = p.next
            if not q:
                return p
            p.next = swap(q.next)
            q.next = p   
            return q
        pre.next = swap(head)
        return pre.next