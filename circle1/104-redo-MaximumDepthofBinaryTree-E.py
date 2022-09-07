'''
104. Maximum Depth of Binary Tree

Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
'''

'''
有点慢：faster than 13.36% of Python3
'''

def maxDepth(root):
    if not root:
        return 0
    layer = 0
    stack = [root]
    while stack:
        temp = []
        for s in stack:
            if s.left:
                temp.append(s.left)
            if s.right:
                temp.append(s.right)
        layer = layer + 1
        stack = temp
    return layer

'''
redo for 递归的思路
'''
# faster than 73.13% of Python3
def maxDepth(root):
    if not root:
        return 0
    return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1