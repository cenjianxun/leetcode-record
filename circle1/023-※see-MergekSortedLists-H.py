'''
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.
'''

'''
边界情况要考虑
1. 第一个为空
2. 尾：其中有一个全完了
3. 首：需要挪head （挪完也需要重新把当前的p往前指
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortOne(self, node, p):
        n = node
        if not node:
            node = p
        if n and p and n.val > p.val:
            new_node = ListNode(p.val) 
            new_node.next = n
            node = new_node
            p = p.next
            n = node
            # print(n.val, p.val)
            
        while p and n:
            if n.next:
                if n.next.val > p.val:
                    new_node = ListNode(p.val)
                    new_node.next = n.next
                    n.next = new_node
                    p = p.next
                else:
                    n = n.next
            else:
                n.next = p
                break
        # print(node.val)
        return node
        
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists:
            return None
        result = lists.pop(0)

        while lists:
            p = lists.pop(0)
            result = self.sortOne(result, p)
        return result

'''
太慢了！
'''
# faster than 9.66% of Python3
def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    if not lists:
        return 
    head = lists.pop()
   
    def merge(p, q):
        if not p or not q:
            return p or q
        if p.val > q.val:
            head = k = q
            q = q.next
        else:
            head = k = p
            p = p.next
        while p and q:
            if p.val > q.val:
                k.next = q
                q = q.next
            else:
                k.next = p
                p = p.next
            k = k.next
        if p:
            k.next = p
        if q:
            k.next = q
        return head
        
    while lists:
        p = head
        q = lists.pop()
        head = merge(p, q)
    return head

'''
用堆
好快！！！

***！！ 重要重要漏洞：
经过push进堆的列，并不是全sorted排列，因为它不稳定，不能直接遍历heap
需要使用heapq.heappop()来遍历
'''

# faster than 93.46% of Python3
def mergeKLists(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    heap = []
    
    for p in lists:
        while p:
            heapq.heappush(heap, p.val)
            p = p.next
    print(heap)      
    head = p = ListNode()
    while heap:
        v = heapq.heappop(heap)
        p.next = ListNode(v)
        p = p.next
    return head.next