'''
You are given a perfect binary tree where all leaves are on the same level, and every parent has two children. The binary tree has the following definition:

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.
'''

def connect(root: 'Node') -> 'Node':
    if not root:
        return root
    stack = [root]
    while stack:
        temp = []
        n = stack.pop(0)
        if n.left:
            temp.append(n.left)
        if n.right:
            temp.append(n.right)
        while stack:
            n.next = stack.pop(0)
            n = n.next
            if n.left:
                temp.append(n.left)
            if n.right:
                temp.append(n.right)
        stack = temp
    return root

'''
用常数级空间！

关键点在于，利用root.next，下级能连通说明上级，本层一定有next，然后绕本层的next去连
'''

def connect(self, root: 'Node') -> 'Node':
    if not root:
        return 
    if root.left:
        root.left.next = root.right
        if root.next:
            root.right.next = root.next.left
    self.connect(root.left)
    self.connect(root.right)
    return root

'''
! 一个节点做不到就用两个节点做！！

def connect(self, root):
    if not root:
        return root:
    self.connectTwo(root.left, root.right)
    rturn root

def connectTwo(self, left, right):
    if not left or not right:
        return None
    left.next = right
    self.connectTwo(left.left, left.right)
    self.connectTwo(right.left, right.right)
    self.connectTwo(left.right, right.left)
'''