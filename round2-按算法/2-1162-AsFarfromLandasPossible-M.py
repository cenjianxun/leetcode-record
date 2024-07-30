'''
1162. As Far from Land as Possible

Given an n x n grid containing only values 0 and 1, where 0 represents water and 1 represents land, find a water cell such that its distance to the nearest land cell is maximized, and return the distance. If no land or water exists in the grid, return -1.

The distance used in this problem is the Manhattan distance: the distance between two cells (x0, y0) and (x1, y1) is |x0 - x1| + |y0 - y1|.
'''

'''
就是一圈一圈往外扩
'''
def maxDistance(self, grid: List[List[int]]) -> int:
    n = len(grid)        
    dis = {}
    seen = {(i, j) for i in range(n) for j in range(n)}
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 1:
                seen.remove((i, j))
                if not 0 in dis:
                    dis[0] = set()
                dis[0].add((i, j))
    if not dis or len(dis[0]) == n * n:
        return -1
    
    while seen:
        d = max(dis.keys())
        for i, j in dis[d]:
            for x, y in ((i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)):
                if 0 <= x < n and 0 <= y < n and (x, y) in seen:
                    seen.remove((x, y))
                    if d + 1 not in dis:
                        dis[d + 1] = set()
                    dis[d + 1].add((x, y))
    return max(dis.keys())