'''
743. Network Delay Time

You are given a network of n nodes, labeled from 1 to n. You are also given times, a list of travel times as directed edges times[i] = (ui, vi, wi), where ui is the source node, vi is the target node, and wi is the time it takes for a signal to travel from source to target.

We will send a signal from a given node k. Return the time it takes for all the n nodes to receive the signal. If it is impossible for all the n nodes to receive the signal, return -1.
'''

'''
Dijkstra 的模板：
需要一个visited，记录走过的
需要一个链表dist，记录每一个节点，从【start】到它的最短路径，初始为正无穷
需要一个graph，记录u->v以及他们的权重
每一轮：
1 筛选出目前为止，没走过的，路径最短的节点s
2 遍历以s为起点的graph，找到s->e的e，并依次比较本身e记录在dist里（即从开头到e的）最短长度+从s到e的权重w，和s的最短长度，即：
dist[s] + dist(从s到e) VS dist[e]
每多走一步，都要全部更新判断，当前每个节点在最短记录里的(从起点的)长度是不是最短，还可不可以更短

最终结束在：如果有正无穷在dist里则返回-1（无法遍历），否则返回max
'''
def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
    graph = defaultdict(list)
    for u, v, w in times:
        graph[u - 1].append((v - 1, w))
    
    receive = [float('inf')] * n
    k = k - 1
    visited = set()
    receive[k] = 0 
    print( graph)
    for _ in range(n):
        smallest = min([(receive[i], i) for i in range(n) if i not in visited])
        visited.add(smallest[1])
        for v, w in graph[smallest[1]]:
            if v not in visited and smallest[0] + w < receive[v]:
                receive[v] = smallest[0] + w
        print(smallest, receive, visited)
    return -1 if float('inf') in receive else max(receive)

'''
bellman ford
'''
def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
    dist = [float('inf')] * n
    dist[K - 1] = 0
    for i in range(N):
        for u, v, w in times:
            u, v = u - 1, v - i
            dist[v] = min(dist[v], dist[u] + w)
    
    return -1 if float('inf') in receive else max(receive)