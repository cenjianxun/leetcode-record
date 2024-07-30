'''
802. Find Eventual Safe States

There is a directed graph of n nodes with each node labeled from 0 to n - 1. The graph is represented by a 0-indexed 2D integer array graph where graph[i] is an integer array of nodes adjacent to node i, meaning there is an edge from node i to each node in graph[i].

A node is a terminal node if there are no outgoing edges. A node is a safe node if every possible path starting from that node leads to a terminal node.

Return an array containing all the safe nodes of the graph. The answer should be sorted in ascending order.
'''

'''
有向环需要三个点标记的原因：
因为第二次遇到同一个点有两种情况：
1.它结束了（合法到结尾但不是环，when a和b都指向c的时候）
2.成环了
所以需要不同的id区别这两种情况
'''
def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
    n = len(graph)
    res = []
    visited = [0] * n
    for i in range(n):
        if self.dfs(graph, i, visited):
            res.append(i)
    return res

def dfs(self, graph, i, visited):
    # print(i, visited)
    if visited[i] !=0:
        return visited[i] == 2
    visited[i] = 1
    flag = True
    for j in graph[i]:   
        flag = self.dfs(graph, j, visited)
        # print(i, j, graph[i], visited)
        if not flag:
            return flag
    visited[i] = 2
    # print(i, visited, flag)
    return flag

'''
另一种方法，倒着，标记end为0，然后断开最后一条边，倒数第二end就变成end，类推，然后最后剩下的，就是答案+
'''