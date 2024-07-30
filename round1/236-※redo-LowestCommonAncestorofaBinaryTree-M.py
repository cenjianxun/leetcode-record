'''
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”
'''
'''
need其他解法
'''
class Solution:
    def preOrder(self, root, preList):
        preList.append(root)
        if root.left:
            self.preOrder(root.left, preList)
        if root.right:
            self.preOrder(root.right, preList)
            
    def inOrder(self, root, inList):
        if root.left:
            self.inOrder(root.left, inList)
        inList.append(root)
        if root.right:
            self.inOrder(root.right, inList)
            
    def postOrder(self, root, postList):
        if root.left:
            self.postOrder(root.left, postList)
        if root.right:
            self.postOrder(root.right, postList)
        postList.append(root)
        
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        preList = []
        self.preOrder(root, preList)
        inList = []
        self.inOrder(root, inList)
        postList = []
        self.postOrder(root, postList)
        
        pre_pi = preList.index(p)
        pre_qi = preList.index(q)
        in_pi = inList.index(p)
        in_qi = inList.index(q)
        post_pi = postList.index(p)
        post_qi = postList.index(q)

        
        if (pre_pi - pre_qi) * (in_pi - in_qi) > 0 and (in_pi - in_qi) * (post_pi - post_qi) and (pre_pi - pre_qi) * (post_pi - post_qi)> 0:
            pre_i = pre_pi if pre_pi < pre_qi else pre_qi   
            in_i, in_j = (in_pi, in_qi) if in_pi < in_qi else (in_qi, in_pi)
            post_i = post_qi if post_pi < post_qi else post_pi
            result = set(preList[:pre_i]) & set(inList[in_i+1:in_j]) & set(postList[post_i+1:])
            return list(result)[0]
        else :
            i = pre_pi if pre_pi < pre_qi else pre_qi
            return preList[i]


'''
没想通

想通了
'''
# faster than 94.34% of Python3
def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    if not root or root == p or root == q:
        return root
    left = self.lowestCommonAncestor(root.left, p, q)
    right = self.lowestCommonAncestor(root.right, p, q)
    if left and right:
        return root
    return left if left else right