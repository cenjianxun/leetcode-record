'''
218. The Skyline Problem
A city's skyline is the outer contour of the silhouette formed by all the buildings in that city when viewed from a distance. Given the locations and heights of all the buildings, return the skyline formed by these buildings collectively.

The geometric information of each building is given in the array buildings where buildings[i] = [lefti, righti, heighti]:

lefti is the x coordinate of the left edge of the ith building.
righti is the x coordinate of the right edge of the ith building.
heighti is the height of the ith building.
You may assume all buildings are perfect rectangles grounded on an absolutely flat surface at height 0.

The skyline should be represented as a list of "key points" sorted by their x-coordinate in the form [[x1,y1],[x2,y2],...]. Each key point is the left endpoint of some horizontal segment in the skyline except the last point in the list, which always has a y-coordinate 0 and is used to mark the skyline's termination where the rightmost building ends. Any ground between the leftmost and rightmost buildings should be part of the skyline's contour.

Note: There must be no consecutive horizontal lines of equal height in the output skyline. For instance, [...,[2 3],[4 5],[7 5],[11 5],[12 7],...] is not acceptable; the three lines of height 5 should be merged into one in the final output as such: [...,[2 3],[4 5],[12 7],...]
'''

'''
先排序，入度的h为负，出度的h为正
循环，如果是入度，就push进大顶堆，匹配（横轴，堆最大值）进result
如果是出度，先删除当前的高度，【然后需要重新排序！】，然后匹配（横轴，堆最大值）进result

结尾需要摒除高一样的非第一个值对。
'''
def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
    # pos = []
    # for pair in buildings:
    #     pos.append((pair[0], -pair[2]))
    #     pos.append((pair[1], pair[2]))
    # pos.sort()
    # # print(pos)
    # heap = []
    # res = []

    # for x, h in pos:
    #     # print('x', x, h, heap, res)
    #     if h < 0 :
    #         heapq.heappush(heap, h)
    #         if h == heap[0]:
    #             res.append([x, -h])
    #     elif h > 0:
    #         heap.remove(-h)
    #         heapq.heapify(heap)
    #         if not heap:
    #             res.append([x, 0])
    #         elif h > -heap[0]:
    #             res.append([x, -heap[0]])
    # preh = 0
    # i = 0
    # while i < len(res):
    #     x, h = res[i]
    #     if preh == h:
    #         res.pop(i)
    #     else:
    #         i = i + 1
    #     preh = h
        
    # return res

    pos = []
    for pair in buildings:
        pos.append((pair[0], -pair[2]))
        pos.append((pair[1], pair[2]))
    pos.sort()
    print(pos)
    heap = []
    res = []
    for x, h in pos:
        # print('x', x, h, heap, res)
        if h < 0 :
            heap.append(-h)
            heap.sort(reverse=True)
            if -h == heap[0]:
                res.append([x, -h])
        elif h > 0:
            heap.remove(h)
            # heapq.heapify(heap)
            if not heap:
                res.append([x, 0])
            elif h > heap[0]:
                res.append([x, heap[0]])
    preh = 0
    i = 0
    while i < len(res):
        x, h = res[i]
        if preh == h:
            res.pop(i)
        else:
            i = i + 1
        preh = h
    return res