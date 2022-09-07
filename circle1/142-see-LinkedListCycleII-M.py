'''
142. Linked List Cycle II

Given the head of a linked list, return the node where the cycle begins. If there is no cycle, return null.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to (0-indexed). It is -1 if there is no cycle. Note that pos is not passed as a parameter.

Do not modify the linked list.
'''

'''
快慢指针第一轮完了之后：
pre: 入环之前的
furword：追上时比起入环点多走的
rest：环周长 - furword

追上：2 * (pre + furword) == pre + furword + rest + furword
-> pre == rest
-> 第二次，一个从头走，一个从第一次相等的点走，将会在入环点相遇
'''
# faster than 81.12% of Python3
def detectCycle(head: ListNode) -> ListNode:
    fast = slow = head
    count_fast, count_slow = 1, 1
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next 
        count_fast, count_slow = count_fast + 2, count_slow + 1
        # print(fast.val, slow.val, count_fast, count_slow)
        if fast == slow:
            break
    if not fast or not fast.next:
        return 
    
    slow = head
    while slow != fast:
        slow = slow.next
        fast = fast.next
    return fast