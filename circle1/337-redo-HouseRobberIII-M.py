'''
337. House Robber III

The thief has found himself a new place for his thievery again. There is only one entrance to this area, called root.

Besides the root, each house has one and only one parent house. After a tour, the smart thief realized that all houses in this place form a binary tree. It will automatically contact the police if two directly-linked houses were broken into on the same night.

Given the root of the binary tree, return the maximum amount of money the thief can rob without alerting the police.
'''

'''
如果超时，就把之前的结果存在dic里
'''

# faster than 44.32% of Python3
def rob(self, root: Optional[TreeNode]) -> int:
    if not root:
        return 0
    mem = {}
    def dfs(root):
        if not root:
            return 0
        if id(root) in mem:
            return mem[id(root)]
        left = right = 0
        if root.left:
            left = dfs(root.left.left) + dfs(root.left.right)
        if root.right:
            right = dfs(root.right.left) + dfs(root.right.right)
        mem[id(root)] = max(root.val + left  + right, dfs(root.left) + dfs(root.right)) 
        return mem[id(root)]       
    dfs(root)
    return mem[id(root)]

'''
这个和线性的一样。cur 取 ppre+nums[i]和pre者大的返回就行，就此不改了。
树不同的是每一个节点的最终值都要计算，是dfs(node),
搞清dfs(node)计算的是什么，就是当前节点返回的最终值。
那么前一(两)个节点就是dfs(node.child) = dfs(node.left) + dfs(node.right)
前前一（四）个节点就是dfs(node.child.child) = dfs(node.left.left) + dfs(node.left.right) + dfs(node.right.left) + dfs(node.right.right)
所以当前公式是 cur = max(ppre+node.val, pre)
代入
'''

'''
树形动态规划，动态规划最重要的一步就是定义状态和对每一种状态进行决策和状态转移，如果能写出状态转移方程并且符合题目要求，那基本上大致思路对的。稍加思索可以发现这题对于每一个结点有取和不取两种状态：

dp[u][0]表示不选当前结点u的情况下以u为根的子树所能得到得最大价值;
dp[u][1]表示选当前结点u的情况下以uu为根的子树所能得到得最大价值.
对于第一种情况，如果不选u，那么u的儿子vi无论选不选都无所谓，因为u已经将他们隔开，因此每个儿子按照贪心的策略应该把自己最大的价值传递给u，即
dp[u][0] = 之和{max(dp[v][0], dp[v][1])}
对于第二种情况，如果选u，那么uu的儿子vi一定不能选，因为相邻的两个点不能同时被选中，因此每个儿子只能把自己不选的价值传递给u，即
dp[u][1] = 之和{dp[v][0]}

最后的答案就是max{dp[u_i][0], dp[u_i][1]}, u属于tree
'''

class Solution:
    def rob(self, root: TreeNode) -> int:
        result = self.rob_tree(root)
        return max(result[0], result[1])
    
    def rob_tree(self, node):
        if node is None:
            return (0, 0) # (偷当前节点金额，不偷当前节点金额)
        left = self.rob_tree(node.left)
        right = self.rob_tree(node.right)
        val1 = node.val + left[1] + right[1] # 偷当前节点，不能偷子节点
        val2 = max(left[0], left[1]) + max(right[0], right[1]) # 不偷当前节点，可偷可不偷子节点
        return (val1, val2)