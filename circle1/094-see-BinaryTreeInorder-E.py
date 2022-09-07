'''
Given the root of a binary tree, return the inorder traversal of its nodes' values.
'''

'''
看一下非遍历的方法
'''

class Solution:
    def test(self, root, result):
        if not root:
            return result
        
        self.test(root.left, result)
        result.append(root.val)
        self.test(root.right, result)
        return result
        
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        result = []
        result = self.test(root, result)
 
        return result



    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack, res = [], []
        while True:
            while root:
                stack.append(root)
                root = root.left
            if not stack:
                return res
            root = stack.pop()
            res.append(root.val)
            root = root.right