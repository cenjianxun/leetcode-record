'''
Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).
'''

'''
1、if else的时候 if not right 和 if left and not right 不同
2、要考虑孙子的情况
'''


class Solution:
    def inOrder(self, root, result):
        if root:
            if root.left and root.right:
                self.inOrder(root.left, result)
                result.append(root.val)
                self.inOrder(root.right, result)
            elif root.right and not root.left:
                # print('nl')
                if root.right.right or root.right.left:
                    result.extend([''] * 3)
                else:
                    result.append('')
                result.append(root.val)
                self.inOrder(root.right, result)    
            elif root.left and not root.right:
                # print('nr')
                self.inOrder(root.left, result)
                result.append(root.val)
                if root.left.right or root.left.left:
                    result.extend([''] * 3)
                else:
                    result.append('')
            elif not root.left and not root.right:
                result.append(root.val)
 
        return result
        
    def isSymmetric(self, root: TreeNode) -> bool:
        left_l = self.inOrder(root.left, [])
        
        right_l = self.inOrder(root.right, [])
        print(left_l)
        print(right_l)
        if left_l == right_l[::-1]:
            return True
        else:
            return False

'''
无语，递归，左的右=右的左
'''

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        return self.helper(root.left, root.right)
    
    def helper(self, left, right):
        if not left and not right:
            return True
        if left and not right or right and not left:
            return False

        '''
        上面两行可以换成：
        if not left or not right:
            return left == right   
        '''
        if left.val != right.val:
            return False
        return self.helper(left.right, right.left) and self.helper(right.right, left.left)

'''
220613
不要局限想说只能递归成为：子树是否对称
递归也可以做到判断整体对称，一直左.左vs右.右就是全局。
'''