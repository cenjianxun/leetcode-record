'''
A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. A node can only appear in the sequence at most once. Note that the path does not need to pass through the root.

The path sum of a path is the sum of the node's values in the path.

Given the root of a binary tree, return the maximum path sum of any path.
'''

'''
全局最大和延续最大是两件事，
延续最大必须可以延续，有三种选择：max(根，根+左，根+右)
全局最大可以中断，可以有很远处的一个局部最大值：max(延续最大，单个左，单个右)
       /*
         * 这个地方可能有点疑惑，你可能会想
         *   -100
         *  19   14
         *  这种情况maxValue肯定还是19，那么为什么还要return 10+（-100）呢？
         *  那是因为maxValue才是我们最终需要的结果，这里的return的只是相当于为更上一级提供了一个接口
         *  给他们提供一种更大的可能性，万一更上面的root是1000，那么这个接口就用上了。就可以获得正确的结果
         *  所以我们这里需要的只是return一个可能性，并不影响最大的结果
         */
'''

'''
测试：[-1,-2,10,-6,null,-3,-6]
'''
class Solution:
        
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 
        self.maxnum = float('-inf')
        maxnum = self.helper(root)
        return max(self.maxnum, maxnum)
    
    def helper(self, root):
        if not root:
            return 0
        left = self.helper(root.left)
        right = self.helper(root.right)
        maxnum = max(max(left, right) + root.val, root.val)
        self.maxnum = max(self.maxnum, root.val, root.val + left + right, maxnum)
        # print(root.val, left, right, maxnum, self.maxnum)
        return maxnum


'''
可以改进的就是，如果子 < 0, 直接赋0就是了
'''
class Solution:
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.current_max = float('-inf')
        self.dp(root)
        return self.current_max

    def dp(self, root):
        if root == None:
            return 0
        left = self.dp(root.left)
        right = self.dp(root.right)

        if not left or left < 0:
            left = 0
        if not right or right < 0:
            right = 0
        self.current_max = max(left + right + root.val, self.current_max)
        return max(left, right) + root.val


'''
220614 see注意细节。
返回值的初始值设定
负数的判定
'''
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxSum = float('-inf')
        maxSum = self.nodeSum(root)
        maxSum = max(self.maxSum, maxSum)
        return maxSum
    
    def nodeSum(self, node):
        if not node :
            return 0
        leftsum = max(0, self.nodeSum(node.left))
        rightsum = max(0, self.nodeSum(node.right))
        
        self.maxSum = max(self.maxSum, node.val + leftsum + rightsum)
        # print(self.maxSum, node.val, leftsum, rightsum)
        return node.val + max(leftsum, rightsum)