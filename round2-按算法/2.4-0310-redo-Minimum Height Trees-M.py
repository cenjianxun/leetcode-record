'''
310. Minimum Height Trees
Medium

A tree is an undirected graph in which any two vertices are connected by exactly one path. In other words, any connected graph without simple cycles is a tree.

Given a tree of n nodes labelled from 0 to n - 1, and an array of n - 1 edges where edges[i] = [ai, bi] indicates that there is an undirected edge between the two nodes ai and bi in the tree, you can choose any node of the tree as the root. When you select a node x as the root, the result tree has height h. Among all possible rooted trees, those with minimum height (i.e. min(h))  are called minimum height trees (MHTs).

Return a list of all MHTs' root labels. You can return the answer in any order.

The height of a rooted tree is the number of edges on the longest downward path between the root and a leaf.

Example 1:

	Input: n = 4, edges = [[1,0],[1,2],[1,3]]
	Output: [1]
	Explanation: As shown, the height of the tree is 1 when the root is the node with label 1 which is the only MHT.

Example 2:

	Input: n = 6, edges = [[3,0],[3,1],[3,2],[3,4],[5,4]]
	Output: [3,4]

Constraints:

	1 <= n <= 2 * 104
	edges.length == n - 1
	0 <= ai, bi < n
	ai != bi
	All the pairs (ai, bi) are distinct.
	The given input is guaranteed to be a tree and there will be no repeated edges.
'''

'''
超时版

原来正常用这个求每个点深度的思路就是会超时

如果将deeps改进为动态dp，需要更新为记录入度高度和出度高度，deeps[i] = max(deeps_in[i], deeps_out[i])
(不太会)
'''

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        deeps = [0] * n
        graph = defaultdict(dict)
        for u, v in edges:
            graph[u][v] = 1
            graph[v][u] = 1
        
        def dfs(node, visited):
            deep = 0
            for u in graph[node]:
                if u not in visited:  
                    deep = max(deep, dfs(u, visited | {u})+1)
            return deep 
        
        short = n
        res = []
        for u in range(n):
            deeps[u] = dfs(u, {u})
            short = min(short, deeps[u])
 
        for i, d in enumerate(deeps):
            if d == short:
                res.append(i)
        return res


'''
拓扑法

由叶子开始减，最终剩下的2个或1个
'''

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n < 2:
            return [0]
        graph = defaultdict(set)
        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)
        
        leavies = [i for i in range(n) if len(graph[i]) ==1]
 
        while n > 2:
            n -= len(leavies)
            temp = []
            for leaf in leavies:
                neighbor = graph[leaf].pop()
                graph[neighbor].remove(leaf)
                if len(graph[neighbor]) == 1:
                    temp.append(neighbor)
            leavies = temp
        return leavies