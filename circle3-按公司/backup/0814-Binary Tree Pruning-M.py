'''
814. Binary Tree Pruning

Given the root of a binary tree, return the same tree where every subtree (of the given tree) not containing a 1 has been removed.

A subtree of a node node is node plus every node that is a descendant of node.

'''

'''
要返回root 和none，不能返回true or false，否则最后如果执行整个函数的结果，还要再判断一次是否是false，如果是false要返回空的，但这时候如果返回root，root里是还有值的。
'''
# faster than 94.89% of Python3
class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def prune(root):
            if not root:
                return None
            root.left = prune(root.left)
            root.right = prune(root.right)

            if not root.left and not root.right and not root.val:
                return None
            return root
        
        return prune(root)

'''
如果不用子函数，外面返回的是root，而不是func(root)
'''
# faster than 94.89% of Python3
class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        if not root:
            return None
        root.left = self.pruneTree(root.left)
        root.right = self.pruneTree(root.right)

        if not root.left and not root.right and not root.val:
            return None
        return root