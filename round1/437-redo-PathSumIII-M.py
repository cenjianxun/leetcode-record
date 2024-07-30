'''
437. Path Sum III

Given the root of a binary tree and an integer targetSum, return the number of paths where the sum of the values along the path equals targetSum.

The path does not need to start or end at the root or a leaf, but it must go downwards (i.e., traveling only from parent nodes to child nodes).
'''

# faster than 38.67% of Python3
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if not root:
            return 0
        self.paths = []
        self.getPath(root, [])
        res = 0
        self.paths = self.paths[::-1]
        # print(self.)
        while self.paths:
            path = self.paths.pop()
            while path:
                res = res + self.sumPath(path, targetSum)
                path.pop()
                if self.paths and set(path).issubset(set(self.paths[-1])):
                    path = []
        return res
                
    def getPath(self, root, path):
        path.append(root)
        if root.left or root.right:
            if root.left:
                self.getPath(root.left, path[:])
            if root.right:
                self.getPath(root.right, path[:])
        else:
            self.paths.append(path)
      
    def sumPath(self, path, targetSum):
        res = 0
        psum = 0
        for p in path[::-1]:
            psum = psum + p.val
            if psum == targetSum:
                res = res + 1
        return res


'''
这里递归的有两层，一层是算本条的和，一层是算（下面的每条的和）
dfs是计算从根节点开始的和为某个值的path的个数，如果我们对树中的所有节点都执行这个方法，那么就相当于查找所有路径和为某个值的方法
'''
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if not root:
            return 0
  
        return self.pathSum(root.left, targetSum) + self.pathSum(root.right, targetSum) + self.dfs(root, targetSum)
        
    def dfs(self, root, rest):
        if not root:
            return 0
        
        count = 1 if root.val == rest else 0
        
        return count + self.dfs(root.left, rest - root.val) + self.dfs(root.right, rest - root.val)