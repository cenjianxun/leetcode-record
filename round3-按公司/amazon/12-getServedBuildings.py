'''
https://leetcode.com/discuss/interview-experience/1972148/amazon-oa-april-2022-served-buildings-number-of-ways-to-choose-3-pages

Find the number of served buildings

Given:

Head count for a list of buildings
Array of range for each router
Array of location of each router
If a router location is i and it's range is k then it will serve buildings at indices i-k to i+k inclusive.

A building is considered as served if the number of routers serving that building is greater than or equal to head count of that building.

Test case 1:
headCount: [2, 3, 3, 1, 5, 6]
routerLocation: [2, 4, 3]
routerRange: [2, 4, 1]

Number of routrers serving each building would be [2, 2, 3, 3, 3, 1] so buildings at indices. 0, 2 and 3 would be considered as served and hence the answer would be 3 (number of served buildings).
'''
'''
差分
'''
def shortestPathBinaryMatrix(headCount, routerLocation, routerRange):
	res = 0
	mark = [0] * (len(headCount)+1)

	for i, r in zip(routerLocation, routerRange):
		start, end = max(0, i - r), min(len(headCount)-1, i + r)
		mark[start] += 1
		mark[end+1] -= 1
		print(i, r, mark)

	tmp = 0
	for i in range(len(headCount)):
		tmp += mark[i]
		mark[i] = tmp
		if mark[i] >= headCount[i]:
			res += 1
	print(mark, res)
	return res

headCount = [2, 3, 3, 1, 5, 6]
routerLocation = [2, 4, 3]
routerRange = [2, 4, 1]
shortestPathBinaryMatrix(headCount, routerLocation, routerRange)