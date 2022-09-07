'''
230. Kth Smallest Element in a BST

Given the root of a binary search tree, and an integer k, return the kth (1-indexed) smallest element in the tree.
'''

def kthSmallest(self, root: TreeNode, k: int) -> int:
    import heapq
    heap = []
    def dfs(root):
        if not root:
            return
        heapq.heappush(heap, -root.val)
        if len(heap) > k:
            heapq.heappop(heap)
        dfs(root.left)
        dfs(root.right)
        # print(heap)
    dfs(root)
    return -heap[0]


'''
BST:
左子树都小于根小于右子树
->BST就用中序遍历
'''
# faster than 80.61% of Python3
class Solution:
    def kthSmallest(self, root, k):
        '''
        中序递归
        '''
        return self.helper(root, k)

    def helper(self, root, k):
        if not root:
            return -1
        val = self.helper(root.left, k)
        if not k:
            return val
        k = k - 1
        if not k:
            return root.val
        self.helper(root.right, k)

# faster than 92.71% of Python3
class Solution:
    def kthSmallest(self, root, k):
        '''
        中序循环
        '''
        stack = []
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            k = k - 1
            if not k:
                return root.val
            root = root.right

'''
如果直接中序，O是O(N),
可以利用bst的性质，在每一步判断它排第几
'''