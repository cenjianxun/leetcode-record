'''
617. Merge Two Binary Trees

You are given two binary trees root1 and root2.

Imagine that when you put one of them to cover the other, some nodes of the two trees are overlapped while the others are not. You need to merge the two trees into a new binary tree. The merge rule is that if two nodes overlap, then sum node values up as the new value of the merged node. Otherwise, the NOT null node will be used as the node of the new tree.

Return the merged tree.

Note: The merging process must start from the root nodes of both trees.
'''


# faster than 36.66% of Python3
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root2:
            return root1
        if not root1:
            return root2
        root = root1
        self.merge(root1, root2)
        return root
        
    def merge(self, root1, root2):
        # print(root1.val, root2.val)
        root1.val = root1.val + root2.val
        
        if root1.left or root2.left:
            if not root1.left:
                root1.left = TreeNode(0)
            if not root2.left:
                root2.left = TreeNode(0)
            # print('l', root1.left.val, root2.left.val)
            self.merge(root1.left, root2.left)
        if root1.right or root2.right:
            if not root1.right:
                root1.right = TreeNode(0)
            if not root2.right:
                root2.right = TreeNode(0)
            # print('r', root1.right.val, root2.right.val)
            self.merge(root1.right, root2.right)

'''
在原地递归还有一个思路：
root.left = self.func(~~~)
root.right = self.func(~~)
return root

这样每一轮的root都不挪动，只是它的下一辈用函数
'''

# faster than 97.32% of Python3
def mergeTrees(self, t1, t2):
    """
    :type t1: TreeNode
    :type t2: TreeNode
    :rtype: TreeNode
    """
    # 结点都为空时
    if t1 is None and t2 is None:
        return
    # 只有一个结点为空时
    if t1 is None:
        return t2
    if t2 is None:
        return t1
    # 结点重叠时
    t1.val += t2.val
    # 进行迭代
    t1.right = self.mergeTrees(t1.right, t2.right)
    t1.left = self.mergeTrees(t1.left, t2.left)
    return t1