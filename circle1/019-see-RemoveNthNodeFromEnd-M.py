'''
Given the head of a linked list, remove the nth node from the end of the list and return its head.
'''

'''
边界条件要注意
1. 减掉的剩的是第几个
2. 减到了head怎么办
'''


def removeNthFromEnd(head: ListNode, n: int) -> ListNode:
    if not head:
        return None
    l = 0
    p = head
    while p:
        p = p.next
        l = l + 1
    hl = l - n

    if not hl:
        return head.next
    hl = hl - 1
    p = head
    # print(hl, l, head.val)
    while hl:
        p = p.next
        hl = hl - 1
    temp = p.next
    p.next = temp.next
    
    return head

'''
** 用快慢指针！！
给定n，fast就先走n步
'''