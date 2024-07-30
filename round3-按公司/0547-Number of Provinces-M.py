'''
547. Number of Provinces
Medium

There are n cities. Some of them are connected, while some are not. If city a is connected directly with city b, and city b is connected directly with city c, then city a is connected indirectly with city c.

A province is a group of directly or indirectly connected cities and no other cities outside of the group.

You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith city and the jth city are directly connected, and isConnected[i][j] = 0 otherwise.

Return the total number of provinces.

Example 1:

	Input: isConnected = [[1,1,0],[1,1,0],[0,0,1]]
	Output: 2

Example 2:

	Input: isConnected = [[1,0,0],[0,1,0],[0,0,1]]
	Output: 3
 

Constraints:

	1 <= n <= 200
	n == isConnected.length
	n == isConnected[i].length
	isConnected[i][j] is 1 or 0.
	isConnected[i][i] == 1
	isConnected[i][j] == isConnected[j][i]
'''

'''
union find
'''

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        provinces = set()
        
        parent = list(range(len(isConnected)))
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        def union(x, y):
            idx, idy = find(x), find(y)
            if idx != idy:
                parent[idx] = idy
                
        for i in range(len(isConnected)):
            for j in range(i, len(isConnected)):
                if isConnected[i][j]:
                    union(i, j)
        for i in range(len(isConnected)):
            idx = find(i)
            if idx not in provinces:
                provinces.add(idx)
        return len(provinces)