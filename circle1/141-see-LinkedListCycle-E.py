'''
Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.
'''

'''
太慢了 faster than 5.01% of Python3
'''

def hasCycle(head) -> bool:
    stack = []
    p = head
    if not p:
        return False
    while p.next:
        if p.next in stack:
            return True
        stack.append(p)
        p = p.next
    return False

# faster than 56.98% of Python3
def hasCycle(head: ListNode) -> bool:
    mark = set()
    p = head
    while p:
        if not p in mark:
            mark.add(p) # 这里可以存node的id，id(p)
        else:
            return True
        p = p.next
        # print(mark)
    return False

'''
follow up:
你能在不使用额外空间的情况下解决吗？
快慢指针
'''

# faster than 56.98% of Python3
def hasCycle(self, head: ListNode) -> bool:
    fast = slow = head
    if not head or not head.next:
        return False
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if fast == slow:
            return True
    return False