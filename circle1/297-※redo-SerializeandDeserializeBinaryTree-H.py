'''
Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.

Clarification: The input/output format is the same as how LeetCode serializes a binary tree. You do not necessarily need to follow this format, so please be creative and come up with different approaches yourself.
'''

'''
这个题的意思是data必须是str，但是不一定是x序遍历，不一定按横着的存，root存进去能变str又能再变回来就行。
一般按中序遍历就行
'''

'''
太慢了
0 和 none
'''

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        result = []
        stack = []
        if not root:
            return result
        stack.append(root)
        while stack:
            temp = []
            while stack:
                r = stack.pop(0)
                if r:
                    result.append(r.val)
                    temp.append(r)
                else:
                    result.append(None)
                 
            while temp:
                r = temp.pop(0)
                if r.left:
                    stack.append(r.left)
                else:
                    stack.append(None)
                if r.right:
                    stack.append(r.right)
                else:
                    stack.append(None)
                # print(result,r.val)
        i = len(result) - 1
        while i >= 0:
            if result[i] != None:
                break
            i = i - 1
        result = result[:i+1]
        return result
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        print(data)
        if not data:
            return 
        data = data[::-1]
        d = data.pop()
        root = TreeNode(d)
        stack = [root]
        while data:
            temp = []
            while stack:
                r = stack.pop(0)
                if data:
                    d = data.pop()
                    if d != None:
                        r.left = TreeNode(d)
                        temp.append(r.left)
                if data:
                    d = data.pop()
                    if d != None:
                        r.right = TreeNode(d)
                        temp.append(r.right)
            stack = temp
        return root


'''
遍历二叉树主要有 2 类方法，分别为深度优先（DFS）和广度优先（BFS）。

在深度优先中，你有又可以使用前序，中序和后序搜索方法，你可以使用递归或者非递归算法实现。对于广度优先算法，一般都会采用非递归的实现方法进行实现。
'''

# https://blog.csdn.net/weixin_45642918/article/details/106791137
# https://www.jb51.net/article/140534.htm

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if root == None:
            return '#,'
        left_str = self.serialize(root.left)
        right_str = self.serialize(root.right)
        return str(root.val) + ',' + left_str + right_str
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        print(data)
        if not data:
            return 
        
        def dfs(queue):
            val = queue.popleft()
            if val == '#':
                return
            node = TreeNode(val)
            node.left = dfs(queue)
            # 下面right这个queue是上面left用剩下的
            node.right = dfs(queue)
            return node
            
        from collections import deque
        queue = deque(data.split(','))
        
        return dfs(queue)