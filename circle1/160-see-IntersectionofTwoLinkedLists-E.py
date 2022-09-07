'''
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the MinStack class:

MinStack() initializes the stack object.
void push(val) pushes the element val onto the stack.
void pop() removes the element on the top of the stack.
int top() gets the top element of the stack.
int getMin() retrieves the minimum element in the stack.
'''

'''
链表问题也要注意边界值，next，最后一个，第一个
'''

def getIntersectionNode(headA: ListNode, headB: ListNode) -> ListNode:
    pa = headA
    pb = headB
    while pa.next:
        pa = pa.next
    while pb.next:
        pb = pb.next
    if pa != pb:
        return None
    p = pa
    if not headA.next:
        return p
    pre_a = ListNode()
    pre_a.next = headA
    pre_b = ListNode()
    pre_b.next = headB
    while pa == pb:
        pa = pre_a
        pb = pre_b
        # print(p.val,pa.val)
        while pa.next != p:
            pa = pa.next
        while pb.next != p:
            pb = pb.next
        if pa == pb:
            p = pa
    return p

'''
相当于给A后面续了一个B，给B后面续了一个A，那么第二轮的时候，两个指针速度就相等了。
此外还可以用栈，过程略。
'''

# faster than 87.77% of Python3
def getIntersectionNode(headA: ListNode, headB: ListNode) -> ListNode:

    """
    :type head1, head1: ListNode
    :rtype: ListNode
    """
    if headA is None or headB is None:
        return None
    pA = headA
    pB = headB
    while pA is not pB:
        pA = headB if pA is None else pA.next
        pB = headA if pB is None else pB.next

    return pA