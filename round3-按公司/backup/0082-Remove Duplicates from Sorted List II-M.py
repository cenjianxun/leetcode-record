'''
82. Remove Duplicates from Sorted List II

Given the head of a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list. Return the linked list sorted as well.
'''

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        pre, p = dummy, head
        while p and p.next:
            if p.val == p.next.val:
                while p and p.next and p.val == p.next.val:
                    p.next = p.next.next
                pre.next = p.next
                p = pre.next
            else:
                pre, p = pre.next, p.next
        return dummy.next

        