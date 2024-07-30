'''
https://leetcode.com/problems/shortest-path-in-binary-matrix/
'''
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1:
            return -1
        m, n = len(grid), len(grid[0])
        visited = set()
        queue = deque([])

        queue.append((0, 0, 1))
        visited.add((0, 0))
        while queue:
            lens = len(queue)
            for _ in range(lens):
                i, j, step = queue.popleft()
                #print(i, j, step)
                if i == m - 1 and j == n - 1:
                    return step
                for x, y in [(i-1,j-1),(i-1,j),(i-1,j+1),(i,j-1),(i,j+1),(i+1,j-1),(i+1,j),(i+1,j+1)]:
                    if 0 <= x < m and 0 <= y < n:
                        if grid[x][y] == 0 and (x, y) not in visited:
                            queue.append((x, y, step + 1))
                            visited.add((x,y))
        return -1