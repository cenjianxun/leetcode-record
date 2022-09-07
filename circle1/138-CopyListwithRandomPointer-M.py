'''
A linked list of length n is given such that each node contains an additional random pointer, which could point to any node in the list, or null.

Construct a deep copy of the list. The deep copy should consist of exactly n brand new nodes, where each new node has its value set to the value of its corresponding original node. Both the next and random pointer of the new nodes should point to new nodes in the copied list such that the pointers in the original list and copied list represent the same list state. None of the pointers in the new list should point to nodes in the original list.

For example, if there are two nodes X and Y in the original list, where X.random --> Y, then for the corresponding two nodes x and y in the copied list, x.random --> y.

Return the head of the copied linked list.

The linked list is represented in the input/output as a list of n nodes. Each node is represented as a pair of [val, random_index] where:

val: an integer representing Node.val
random_index: the index of the node (range from 0 to n-1) that the random pointer points to, or null if it does not point to any node.
Your code will only be given the head of the original linked list.
'''

'''
慢 其他方法 faster than 16.56% of Python3 

'''

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        p = head
        stack_p = []
        stack_q = []
        cnode = q = Node(0)
        i = 0
        while p:
            q.next = Node(p.val)
            q = q.next
            stack_p.append(p)
            stack_q.append(q)
            p = p.next
        p = head
        q = cnode.next
        for i in range(0, len(stack_p)):
            if stack_p[i].random:
                ni = stack_p.index(stack_p[i].random)
                q.random = stack_q[ni]
            q = q.next
        return cnode.next

'''
可以把node存在一个dict里 dict[当前结点] = 新结点
'''

def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
    if not head:
        return 
    node = Node(head.val)
    p, q = head, node
    head_to_node = {head:node}
    while p.next:
        q.next = Node(p.next.val)
        q, p = q.next, p.next
        head_to_node[p] = q
    p, q = head, node
    while p:
        if p.random:
            q.random = head_to_node[p.random]
        q, p = q.next, p.next
    return node 