'''
21. Merge Two Sorted Lists

Merge two sorted linked lists and return it as a sorted list. The list should be made by splicing together the nodes of the first two lists.
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# faster than 75.23% of Python3
def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
    if not l1 or not l2:
        return l1 or l2
    p = l1
    q = l2
    result = ListNode(0)
    k = result
    while p and q:
        if p.val > q.val:
            k.next = ListNode(q.val)
            q = q.next
        else:
            k.next = ListNode(p.val)
            p = p.next 
        k = k.next
    k.next = p if p else q
    return result.next