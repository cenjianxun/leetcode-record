'''
105. Construct Binary Tree from Preorder and Inorder Traversal

Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree.
'''

'''
慢faster than 19.68% of Python3
看看其他解法
'''

def getTree(preorder, inorder, root):
    r = preorder.pop(0)
    root.val = r
    i = inorder.index(r)
    left_in = inorder[0:i]
    right_in = inorder[i+1:]
    left_pre = preorder[:len(left_in)]
    right_pre = preorder[len(left_in):]
    if left_in:
        node = TreeNode(0)
        node = self.getTree(left_pre, left_in, node)
        root.left = node
    if right_in:
        node = TreeNode(0)
        node = self.getTree(right_pre, right_in, node)
        root.right = node
    return root
    
def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
    root = TreeNode(0)
    head = root
    if preorder:
        root = self.getTree(preorder, inorder, root)
    return head


'''
看看递归
'''
def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
    if not preorder or not inorder:
        return None
    root = TreeNode(preorder[0])
    index = inorder.index(preorder[0])
    root.left = self.buildTree(preorder[1:index+1], inorder[:index])
    root.right = self.buildTree(preorder[index+1:], inorder[index+1:])
    return root

'''
这个好快，但没get（get了一点
'''
def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
    def build(stop):
        if inorder and inorder[-1] != stop:
            root = TreeNode(preorder.pop())
            root.left = build(root.val)
            inorder.pop()
            root.right = build(stop)
            return root
    preorder.reverse()
    inorder.reverse()
    return build(None)


'''
see 是see：
为什么想出来的是两层函数
'''
def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
    def build(preorder, inorder):
        if not preorder:
            return
        node = TreeNode(preorder[0])
        i = 0
        while inorder[i] != preorder[0]:
            i += 1
        node.left = build(preorder[1:i+1], inorder[:i])
        node.right = build(preorder[1+i:], inorder[i+1:])
        return node

    return build(preorder, inorder)