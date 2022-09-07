'''
226. Invert Binary Tree

Given the root of a binary tree, invert the tree, and return its root.
'''


def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
    res = []
    if not root:
        return root
    stack = [root]
    while stack:
        temp = []
        while stack:
            node = stack.pop()
            node.left, node.right = node.right, node.left
            node.left and temp.append(node.left)
            node.right and temp.append(node.right)
        stack = temp
    return root



'''
主要是看递归

注意不能交换值，因为有可能一边儿有一边儿没有的情况
'''
def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
    if root:
        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
    return root