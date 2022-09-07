'''
206. Reverse Linked List

Given the head of a singly linked list, reverse the list, and return the reversed list.
'''

'''
最尾一个 要指空
'''


def reverseList(head: ListNode) -> ListNode:
    if not head:
        return head
    stack = []
    p = head 
    while p:
        stack.append(p)
        p = p.next
    node = p = stack.pop()
    while stack:
        p.next = stack.pop()
        print(p.val, p.next.val)
        p = p.next
    p.next = None
    return node


'''
另外一个方式
'''
# faster than 87.45% of Python3
def reverseList( head: ListNode) -> ListNode:
    newp = None
    while head:
        p = head
        head = head.next
        p.next = newp
        newp = p
    return newp