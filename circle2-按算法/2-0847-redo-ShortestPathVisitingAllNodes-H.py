'''
847. Shortest Path Visiting All Nodes

You have an undirected, connected graph of n nodes labeled from 0 to n - 1. You are given an array graph where graph[i] is a list of all the nodes connected with node i by an edge.

Return the length of the shortest path that visits every node. You may start and stop at any node, you may revisit nodes multiple times, and you may reuse edges.
'''

'''
值得重做
特殊在，不是不能重复遍历，而是不能漏，遍历过的可以再次遍历。
->用二进制解决。
相应位置1，如果再次遇到1就continue；
如果1的和（个数）为2**n-1，即为没有漏掉；
储存的时候，存i和该i的state，state就是2进制下i表示为的数；
标记矩阵存的内容为： 节点的个数 x 每个节点都有（2**n）个状态，
意思是，横：以每个节点为起点，竖：以该节点为起点时，需要记录每个节点（2进制意义下）有么有被遍历。

另外一个是bfs时stack的更新，因为又需要遍历又需要append
先算stack的长度，再遍历range(s)， 遍历时先leftpop
'''
def shortestPathLength(self, graph: List[List[int]]) -> int:
    N = len(graph)
    que = collections.deque()
    step = 0
    goal = (1 << N) - 1
    visited = [[0 for j in range(1 << N)] for i in range(N)]
    print(goal)
    for i in range(N):
        que.append((i, 1 << i))

    while que:
        s = len(que)
        print(que)
        for i in range(s):
            node, state = que.popleft()
            
            if state == goal:
                print(node, state, visited)
                return step
            if visited[node][state]:
                continue
            visited[node][state] = 1
            print(node, state, visited[node])
            for nextNode in graph[node]:
                print(node, nextNode)
                que.append((nextNode, state | (1 << nextNode)))
        step += 1
    return step