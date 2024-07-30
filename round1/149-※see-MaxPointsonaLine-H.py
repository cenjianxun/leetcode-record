'''
149. Max Points on a Line

Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane, return the maximum number of points that lie on the same straight line.
<———— maximum number 同条线上的最多的个数，而不是最大值
'''

'''
1. 不是只有斜率就行，k, b都要有
2. 注意垂直的情况
'''

def maxPoints(points: List[List[int]]) -> int:
    dic = {}
    if len(points) == 1:
        return 1
    for i in range(0, len(points)-1):
        for j in range(i+1, len(points)):
            # print(i, j)
            if points[j][0] == points[i][0]:
                k = 'h'
                b = points[i][0]
            else:
                k = (points[j][1] - points[i][1])/(points[j][0] - points[i][0])
                b = points[i][1] - k * points[i][0]
            if not (k,b) in dic:
                dic[(k,b)] = []
            dic[(k,b)].extend([i, j])
            # print(i,j,dic)
    result = 0
    for k in dic:
        # print(dic[k])
        n = len(set(dic[k]))
        result = max(result, n)
    return  result