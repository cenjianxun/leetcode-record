'''
1325. Delete Leaves With a Given Value

Given a binary tree root and an integer target, delete all the leaf nodes with value target.

Note that once you delete a leaf node with value target, if it's parent node becomes a leaf node and has the value target, it should also be deleted (you need to continue doing that until you can't).
'''
'''
这个方法没有cover到边界
'''
def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:

    def dfs(root, target):
        if not root.left and not root.right:
            return 1 if root.val == target else 0
        if root.left:
            left = dfs(root.left, target)
            if left:
                root.left = None
        if root.right:
            right = dfs(root.right, target)
            if right:
                root.right = None
        if not root.left and not root.right and root.val == target:
            return 1
        else:
            return 0
    node = dfs(root, target)
    if node:
        return None
    else:
        return root

'''
改进：
区别：
👆 在下层判断，在上层赋值
👇 在下层直接判断并赋值，上层只收到一个接口就行了
'''
def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:

    def helper(root):
        if not root:
            return None
        left, right = helper(root.left), helper(root.right)
        root.left = left
        root.right = right
        if not left and not right and root.val == target:
            return None
        return root
    return helper(root)
