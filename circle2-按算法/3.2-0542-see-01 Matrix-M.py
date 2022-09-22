'''
542. 01 Matrix
Medium

Given an m x n binary matrix mat, return the distance of the nearest 0 for each cell.

The distance between two adjacent cells is 1.

Example 1:

	Input: mat = [[0,0,0],[0,1,0],[0,0,0]]
	Output: [[0,0,0],[0,1,0],[0,0,0]]
Example 2:

	Input: mat = [[0,0,0],[0,1,0],[1,1,1]]
	Output: [[0,0,0],[0,1,0],[1,2,1]]
	 
Constraints:

	m == mat.length
	n == mat[i].length
	1 <= m, n <= 104
	1 <= m * n <= 104
	mat[i][j] is either 0 or 1.
	There is at least one 0 in mat.
'''

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        res = [[float('inf')] * n for _ in range(m)]
        visited = set()
        queue = deque([])
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    queue.append((i, j, 0))
                    visited.add((i, j))
        while queue:
            i, j, step = queue.popleft()
            res[i][j] = min(res[i][j], step)
            for x, y in [(i, j+1), (i, j-1), (i+1, j), (i-1, j)]:
                if 0 <= x < m and 0 <= y < n and (x, y) not in visited:
                    queue.append((x, y, step + 1))
                    visited.add((x, y))
        return res