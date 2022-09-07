'''
Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
'''

'''
二叉查找树：
1.左边所有的值都小于根；右边所有的值都大于根
2.空树是true
'''
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        
        stack = []
        stack = self.inOrder(root, stack)
        print(stack)
        for i in range(1, len(stack)):
            if stack[i-1] >= stack[i]:
                return False
        return True
            
            
    def inOrder(self, root, stack):
        if not root:
            return
        self.inOrder(root.left, stack)
        stack.append(root.val)
        self.inOrder(root.right, stack)
        return stack