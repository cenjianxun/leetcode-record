'''
199. Binary Tree Right Side View

Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.
'''

'''
see的点很无厘头：
1.[None] 不算空，所以碰到要把参数装入[]，需要单独讨论参数为None的情况
2.deque可以直接初始化
3.将temp赋值给queue时要记得变为deque

* 可以不用temp， 使用for循环
'''

# faster than 7.53% of Python3
def rightSideView(self, root: Optional[TreeNode]) -> List[int]: 
    from collections import deque
    res = []
    if not root:
        return res
    queue = deque([root])
    # print(type(queue))
    while queue:
        print(queue)
        res.append(queue[-1].val)
        temp = []
        while queue:
            p = queue.popleft()
            # print(p.val)
            p.left and temp.append(p.left)
            p.right and temp.append(p.right)
            
        queue = deque(temp)
    return res