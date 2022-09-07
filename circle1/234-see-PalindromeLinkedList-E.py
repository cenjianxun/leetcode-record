'''
Given the head of a singly linked list, return true if it is a palindrome.
'''

'''
看看其他解法:
1. 前半段出栈
2. 后半段反转链表
'''

def isPalindrome(head: ListNode) -> bool:
    p = head
    stack = []
    while p:
        stack.append(p.val)
        p = p.next
    i = 0
    j = len(stack) - 1
    while i<=j and stack[i] == stack[j]:
        i = i + 1
        j = j - 1
    if i > j:
        return True
    else:
        return False

'''
# 快慢指针法找链表的中点
slow = fast = head
while fast and fast.next:
    new_list.insert(0, slow.val)
    slow = slow.next
    fast = fast.next.next

if fast: # 链表有奇数个节点
    slow = slow.next

注意分奇偶：
快慢指针：
奇：fast在最后一个，奇在最中间
偶：fast在第一个空，slow在第二组第一个
'''