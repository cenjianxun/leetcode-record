'''
882. Reachable Nodes In Subdivided Graph

You are given an undirected graph (the "original graph") with n nodes labeled from 0 to n - 1. You decide to subdivide each edge in the graph into a chain of nodes, with the number of new nodes varying between each edge.

The graph is given as a 2D array of edges where edges[i] = [ui, vi, cnti] indicates that there is an edge between nodes ui and vi in the original graph, and cnti is the total number of new nodes that you will subdivide the edge into. Note that cnti == 0 means you will not subdivide the edge.

To subdivide the edge [ui, vi], replace it with (cnti + 1) new edges and cnti new nodes. The new nodes are x1, x2, ..., xcnti, and the new edges are [ui, x1], [x1, x2], [x2, x3], ..., [xcnti-1, xcnti], [xcnti, vi].

In this new graph, you want to know how many nodes are reachable from the node 0, where a node is reachable if the distance is maxMoves or less.

Given the original graph and maxMoves, return the number of nodes that are reachable from node 0 in the new graph.
'''

'''
hashmap就是dict，可以嵌套
max，min可以设置空时的返回值，default = xxx
'''

import heapq
class Solution:
    def reachableNodes(self, edges: List[List[int]], maxMoves: int, n: int) -> int:
        # res = 0
        graph = defaultdict(dict)
        visited = [[0] * n for _ in range(n)]
        visited[0][0] = 1
        points = deque([(0, maxMoves)])
        lefts = {}
        for u, v, w in edges:
            graph[u][v] = graph[v][u] = w
            lefts[u] = lefts[v] = (0, 0)
        lefts[0] = (maxMoves, maxMoves)
        for _ in range(n):
            # print(lefts)
            leftmax = max([(moves[0], u) for u, moves in lefts.items() if moves[0] > 0], default=(0, 0))
            moves, u = leftmax
            if moves == 0:
                break
            for v, w in graph[u].items():
                if visited[u][v] >= moves:
                    continue
                if visited[u][v] + visited[v][u] == w:
                    left = moves - w
                else:
                    left = max(0, moves - (w - (visited[u][v] + visited[v][u])))
                    visited[u][v] += min(moves, w - (visited[u][v] + visited[v][u]))
                if left:
                    left = left - 1
                    if left > lefts[v][1]:
                        lefts[v] = ( max(left, lefts[v][0]), left)
                    visited[v][v] = 1
            lefts[u] = (0, lefts[u][1])

        return sum(sum(visited[i]) for i in range(n))
                        

    def reachableNodes(self, edges, M, N):
        e = collections.defaultdict(dict)
        for i, j, l in edges: e[i][j] = e[j][i] = l
        pq = [(-M, 0)]
        seen = {}
        while pq:
            moves, i = heapq.heappop(pq)
            if i not in seen:
                seen[i] = -moves
                for j in e[i]:
                    moves2 = -moves - e[i][j] - 1
                    if j not in seen and moves2 >= 0:
                        heapq.heappush(pq, (-moves2, j))
        res = len(seen)
        for i, j, k in edges:
            res += min(seen.get(i, 0) + seen.get(j, 0), e[i][j])
        return res

'''
抄袭：
'''
import heapq
class Solution:
    def reachableNodes(self, edges: List[List[int]], maxMoves: int, n: int) -> int:
        graph = defaultdict(dict)
        visited = {}
        for u, v, w in edges:
            graph[u][v] = graph[v][u] = w
        hp = [(-maxMoves, 0)]
        while hp:
            moves, u = heapq.heappop(hp)
            moves = -moves
            if u not in visited:
                print(u, moves)
                visited[u] = moves
                for v, w in graph[u].items():
                    left = moves - w - 1
                    print(u, v, w, left)
                    if v not in visited and left >= 0:
                        heapq.heappush(hp, (-left, v))
       
        res = len(visited)
        for u, v, w in edges:
            res += min(visited.get(u, 0) + visited.get(v, 0), w)
        return res 