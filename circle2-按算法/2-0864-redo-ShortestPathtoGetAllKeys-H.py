'''
864. Shortest Path to Get All Keys
'''

'''
如果是可以重复走格子的问题，
-> 如果只有横纵坐标不能保证唯一性，就引进新的flag，比如keys，比如step
stack和visited里的元素可以依需求加变量参数 
'''
def shortestPathAllKeys(self, grid: List[str]) -> int:
    m, n  = len(grid), len(grid[0]) 
    steps, numOfKeys = 0, 0
    visited =  set()
     
    for i in range(m):
        for j in range(n):
            if grid[i][j] == '@':
                start = (i, j, '')
            if grid[i][j].islower():
                numOfKeys += 1    
    stack = deque([start])
    while stack:
        s = len(stack)
        # print(stack)
        for _ in range(s):
            i, j, keys = stack.popleft()
            if (i, j, keys) in visited:
                continue
            if len(keys) == numOfKeys:
                return steps
            visited.add((i, j, keys))
            for x, y in ((i+1, j), (i-1, j), (i, j+1), (i, j-1)):
                if 0 <= x < m and 0 <= y < n and grid[x][y] != '#':
                    cell = grid[x][y]
                    if cell in '.@' or cell in 'ABCDEF' and cell.lower() in keys:
                        stack.append((x, y, keys))
                    if cell in 'abcdef':
                        if cell not in keys:
                            stack.append((x, y, keys + cell))
                        else:
                            stack.append((x, y, keys))
        steps = steps + 1
    return -1