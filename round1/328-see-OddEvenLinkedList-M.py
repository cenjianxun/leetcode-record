'''
Given the head of a singly linked list, group all the nodes with odd indices together followed by the nodes with even indices, and return the reordered list.

The first node is considered odd, and the second node is even, and so on.

Note that the relative order inside both the even and odd groups should remain as it was in the input.

You must solve the problem in O(1) extra space complexity and O(n) time complexity.
'''

'''
细节：
1 开头
2 进入条件 p本身需要存在
'''

def oddEvenList(head: ListNode) -> ListNode:
    o = p = head
    if not head or not head.next:
        return head
    e = q = head.next

    while p and p.next or q and q.next:
        if p and p.next:
            p.next = p.next.next
        if p.next:
            p = p.next
        if q and q.next:
            q.next = q.next.next
            q = q.next
    p.next = e
    return o


def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    if not head or not head.next:
        return head
    o, e, p = head, head.next, head.next
    while o and o.next:
        o.next = o.next.next
        if o.next: # 注意要加条件
            o = o.next
        if e and e.next: # 注意要加条件
            e.next = e.next.next
            e = e.next
    o.next = p
    return head