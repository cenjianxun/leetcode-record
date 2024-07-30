'''
958. Check Completeness of a Binary Tree

Given the root of a binary tree, determine if it is a complete binary tree.

In a complete binary tree, every level, except possibly the last, is completely filled, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.
'''

# faster than 66.78% of Python3
from collections import deque
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        queue = [root]
        layer = 0
        while queue:
            temp = []
            for node in queue:
                if node.right and not node.left:
                    return False
                temp.append(node.left or -1)
                temp.append(node.right or -1)
            while temp and temp[-1] == -1:
                temp.pop()
            if -1 in temp:
                return False
            if len(queue) < 2**layer and temp:
                return False
            queue = temp
            layer += 1
        return True


'''
简洁：只要none的后面还有值就false
'''

class Solution:
    def isCompleteTree(self, root: TreeNode) -> bool:
        have_null = False
        Q = [root]
        
        while Q:
            cur_node = Q.pop(0)
            if not cur_node: 
                have_null = True
                continue
            if have_null: return False
            Q.append(cur_node.left)
            Q.append(cur_node.right)
            
        return True