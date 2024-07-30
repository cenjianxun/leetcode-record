'''
1110. Delete Nodes And Return Forest
Medium

Given the root of a binary tree, each node in the tree has a distinct value.

After deleting all nodes with a value in to_delete, we are left with a forest (a disjoint union of trees).

Return the roots of the trees in the remaining forest. You may return the result in any order.

Example 1:

	Input: root = [1,2,3,4,5,6,7], to_delete = [3,5]
	Output: [[1,2,null,4],[6],[7]]

Example 2:

	Input: root = [1,2,4,null,3], to_delete = [3]
	Output: [[1,2,4]]
 
Constraints:

	The number of nodes in the given tree is at most 1000.
	Each node has a distinct value between 1 and 1000.
	to_delete.length <= 1000
	to_delete contains distinct values between 1 and 1000.
'''

'''
怎么这么长
'''

# faster than 56.62% of Python3
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        if not root:
            return
        res = []
        to_delete = set(to_delete)
        self.wait = [root]
        def dfs(parent, child, direct):
            if child:
                if child.val in to_delete:
                    self.wait.append(child.left)
                    self.wait.append(child.right)
                    if direct == 'left':
                        parent.left = None
                    else:
                        parent.right = None
                else:
                    dfs(child, child.left, 'left')
                    dfs(child, child.right, 'right')
 
        while self.wait:
            node = self.wait.pop()
            if not node:
                continue
            if node.val in to_delete:
                self.wait.append(node.left)
                self.wait.append(node.right)
            else:
                res.append(node)
                dfs(node, node.left, 'left')
                dfs(node, node.right, 'right')
        return res


'''
需要知道父和子才能改变两者关系的，关系不变，子变
就=> node.left = func(node.left), 利用函数改变
那么改变的状态有什么？原node，和None，那就分别按照条件判断返回值。
此外判断出这个结果还需要什么条件？将这个条件加入参数
'''
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        if not root:
            return
        self.res = []
        to_delete = set(to_delete)
        
        def dfs(node, isroot):
            if not node:
                return None
            if node.val not in to_delete:              
                if isroot:
                    self.res.append(node) 
                isroot = False
                node.left = dfs(node.left, isroot)
                node.right = dfs(node.right, isroot)
                return node
            else:
                isroot = True
                node.left = dfs(node.left, isroot)
                node.right = dfs(node.right, isroot)                
                return None
        dfs(root, True)
        
        return self.res