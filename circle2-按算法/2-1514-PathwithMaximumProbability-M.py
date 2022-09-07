'''
1514. Path with Maximum Probability

You are given an undirected weighted graph of n nodes (0-indexed), represented by an edge list where edges[i] = [a, b] is an undirected edge connecting the nodes a and b with a probability of success of traversing that edge succProb[i].

Given two nodes start and end, find the path with the maximum probability of success to go from start to end and return its success probability.

If there is no path from start to end, return 0. Your answer will be accepted if it differs from the correct answer by at most 1e-5.
'''

from collections import deque
class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        weight = [0] * n
        weight[start] = 1
        graph = defaultdict(set)
        for i in range(len(edges)):
            u, v = edges[i]
            graph[u].add((v, succProb[i]))
            graph[v].add((u, succProb[i]))
        stack = deque([start])
        print(graph)
        while stack:
            s = len(stack)
            for _ in range(s):
                u = stack.popleft()
                # if u == end:
                #     return weight[u]
                if u in graph:
                    for v, w in graph[u]:
                        # print(u, v, weight)
                        if weight[u] * w > weight[v]:
                            weight[v] = weight[u] * w
                            stack.append(v)
                        # print(u, v, weight)
        return weight[end]

'''
改了一点
while 每次只出一个 可以
除非 stack是heap
'''
from collections import deque
class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        weight = [0] * n
        weight[start] = 1
        graph = defaultdict(set)
        for i in range(len(edges)):
            u, v = edges[i]
            graph[u].add((v, succProb[i]))
            graph[v].add((u, succProb[i]))
        stack = deque([start])
        print(graph)
        while stack:
            u = stack.popleft()
            if u not in graph or  u == end:
                continue
            for v, w in graph[u]:
                # print(u, v, weight)
                if weight[u] * w > weight[v]:
                    weight[v] = weight[u] * w
                    stack.append(v)
        return weight[end]