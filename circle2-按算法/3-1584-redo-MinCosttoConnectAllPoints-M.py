'''
1584. Min Cost to Connect All Points

You are given an array points representing integer coordinates of some points on a 2D-plane, where points[i] = [xi, yi].

The cost of connecting two points [xi, yi] and [xj, yj] is the manhattan distance between them: |xi - xj| + |yi - yj|, where |val| denotes the absolute value of val.

Return the minimum cost to make all points connected. All points are connected if there is exactly one simple path between any two points.
'''

'''
超时了
'''
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        if n == 1:
            return 0
        dist = [[0] * n for _ in range(n)]
        res = float('inf')
        to_seen = []
        p = q = 0
        for i in range(n):
            for j in range(i + 1, n):
                d = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                dist[i][j] = dist[j][i] = d
                if d < res:
                    p, q =  i, j
                    res = d
        visited = {p, q}
        dist[p][q] = dist[q][p] = 0
        while len(visited) < n:
            d, p, q = (float('inf'), 0, 0)
            for p in visited:
                short = min([(dist[p][q], p, q) for q in range(n) if dist[p][q]])
                if short[0] < d:
                    d, p, q = short
       
            res += d
            for k in visited:
                dist[p][k] = dist[q][k] = dist[k][p] = dist[k][q] = 0
            dist[p][q] = dist[q][p] = 0
            visited.add(p)
            visited.add(q)
        return res

'''
prim:
一开始可以用一个（0，0)代表(p, q) 然后只管q
从q开始遍历与q相接的点
如果q在seen里，就跳过
'''
import heapq
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        res, n = 0, len(points)
        manhattan = lambda x, y: abs(x[0]-y[0]) + abs(x[1]-y[1])
        seen, hp = set(), [(0, (0, 0))]
        while len(seen) < n:
            w, (p, q) = heapq.heappop(hp)
            if q in seen:
                continue
            res += w
            seen.add(q)
            for i in range(n):
                if i not in seen and i != q:
                    heapq.heappush(hp, (manhattan(points[q], points[i]), (q, i)))
        
        return res

'''
kruskal:
更慢
这里union多加一个判断 true or false，
因为这里是判断不能成环，如果已经成环，就false
'''
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        edges = []
        
        for i in range(n):
            for j in range(i+1, n):
                d = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                edges.append((d, i, j))
        
        edges.sort()
        
        roots = [i for i in range(n)]
        
        def find(v):
            if roots[v] != v:
                roots[v] = find(roots[v])
            return roots[v]
        
        def union(u, v):
            p1 = find(u); p2 = find(v)
            if p1 != p2:
                roots[p2] = roots[p1]
                return True
            return False
        
        res = 0
        for d, u, v in edges:
            if union(u, v):
                res += d
        return res