'''
399. Evaluate Division

You are given an array of variable pairs equations and an array of real numbers values, where equations[i] = [Ai, Bi] and values[i] represent the equation Ai / Bi = values[i]. Each Ai or Bi is a string that represents a single variable.

You are also given some queries, where queries[j] = [Cj, Dj] represents the jth query where you must find the answer for Cj / Dj = ?.

Return the answers to all queries. If a single answer cannot be determined, return -1.0.

Note: The input is always valid. You may assume that evaluating the queries will not result in division by zero and that there is no contradiction.
'''

'''
union-find 这里有倍数，所以find返回值和倍数，union有三个值，a、b和它俩的倍数
后面要判断值是否在parent里，所以parent用map
'''

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        parent = {}
        times = {}
        
        def union(a, b, c):
            root_a, v_a = find(a)
            root_b, v_b = find(b)
            parent[root_a] = root_b
            """ some math here
            a / b = v
            a / root_a = v_a
            b / root_b = v_b
            => root_a / root_b = a * v_b / b / v_a
            """
            times[root_a] = c * v_b / v_a
            
        def find(a):
            if parent[a] != a:
                parent[a], c = find(parent[a])
                times[a] = times[a] * c
            return parent[a], times[a]
        
        for (a, b), c in zip(equations, values):
            if not a in parent:
                parent[a], times[a] = a, 1
            if not b in parent:
                parent[b], times[b] = b, 1
            union(a, b, c)
        
        res = []
        
        for a, b in queries:
            if a not in parent or b not in parent:
                res.append(-1)
                continue
            root_a, v_a = find(a)
            root_b, v_b = find(b)
            res.append(v_a/v_b if root_a == root_b else -1)
            
        return res