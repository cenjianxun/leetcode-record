'''
235. Lowest Common Ancestor of a Binary Search Tree
Easy
 
Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”
'''

'''
其实是默认pq一定会存在在root里
'''
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
 
        if p.val > q.val:
            p, q = q, p
        def search(node, target):
            if not node:
                return 
            if node == target:
                return node
            if node.val > target.val:
                left = search(node.left, target)
                if left == target:
                    return left
            if node.val < target.val:
                right = search(node.right, target)
                if right == target:
                    return right
        while root.val < p.val or root.val > q.val:
            if root.val < p.val:
                root = root.right
            elif root.val > q.val:
                root = root.left
        left = search(root, p)
        right = search(root, q)
        if left == p and right == q:
            return root
        else:
            return -1


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return 
        if root.val > max(p.val, q.val):
            return self.lowestCommonAncestor(root.left, p, q)
        elif root.val < min(p.val, q.val):
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            return root