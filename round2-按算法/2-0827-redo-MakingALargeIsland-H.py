'''
827. Making A Large Island

You are given an n x n binary matrix grid. You are allowed to change at most one 0 to be 1.

Return the size of the largest island in grid after applying this operation.

An island is a 4-directionally connected group of 1s.
'''

'''
主要是超时
要分块。记录每一个island为不同的编号
'''
def largestIsland(self, grid: List[List[int]]) -> int:
    res = 0 
    n = len(grid)
    visited = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
    area = []
    border = defaultdict(set)
    def dfs(i, j, gid):
        visited[i][j] = True
        area = 1
        for x, y in ((i + 1, j), (i -1, j), (i, j + 1), (i, j - 1)):
   
            if 0 <= x < len(grid) and 0 <= y < len(grid[0]):
                if grid[x][y] == 0:
                    border[(x, y)].add(gid)
                    gids[x][y] = gid
                if grid[x][y] == 1 and not visited[x][y]:
                    area += dfs(x, y, gid)
        return area
    gids = [['' for _ in range(len(grid[0]))] for _ in range(len(grid))]
    gid = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1 and not visited[i][j]:
                area.append(dfs(i, j, gid))
                gid += 1

    
    if border:
        return max(1+sum(area[x] for x in y) for y in border.values())
    else:
        return n*n if grid[0][0]==1 else 1