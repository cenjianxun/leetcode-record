'''
148. Sort List

Given the head of a linked list, return the list after sorting it in ascending order.

Follow up: Can you sort the linked list in O(n logn) time and O(1) memory (i.e. constant space)?
'''

'''
使用归并。（不知道为什么
小技巧：想要slow前一个指针的时候，可以在循环中记录pre = slow
'''
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:      
        if not head or not head.next:
            return head

        fast = slow = head
        while fast and fast.next:
            pre = slow
            fast = fast.next.next
            slow = slow.next
        pre.next = None
        right = self.sortList(slow)
        left = self.sortList(head)
        return self.merge(left, right)
            
    def merge(self, left, right):
        
        head = p = ListNode()
        while left and right:
            if left.val < right.val:
                p.next = left
                left = left.next
            else:
                p.next = right
                right = right.next
            p = p.next
        if left:
            p.next = left
        if right:
            p.next = right
        return head.next