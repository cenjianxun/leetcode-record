'''
25. Reverse Nodes in k-Group

Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.

You may not alter the values in the list's nodes, only nodes themselves may be changed.
'''

'''
jump.next, jump, l = pre, l, r, basically assign three variables. First is assigning jump.next = pre. This is equivalent to assign ListNode(0).next = new head after this first iteration. At this point, dummy still point to ListNode(0). So dummy.next points to the new head after this first iteration.

As the iterations going on, jump is assigned to other nodes in each iteration. So jump.next is manipulating other nodes not the ListNode(0). Meanwhile, dummy still point to ListNode(0). So dummy.next always points to the new head after the first iteration.
'''
def reverseKGroup(self, head, k):
    dummy = jump = ListNode(0)
    dummy.next = l = r = head
    
    while True:
        count = 0
        while r and count < k:   # use r to locate the range
            r = r.next
            count += 1
        if count == k:  # if size k satisfied, reverse the inner linked list
            pre, cur = r, l
            for _ in range(k):
                cur.next, cur, pre = pre, cur.next, cur  # standard reversing
            jump.next, jump, l = pre, l, r  # connect two k-groups
        else:
            return dummy.next