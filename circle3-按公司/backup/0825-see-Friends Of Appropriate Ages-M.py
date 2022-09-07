'''
825. Friends Of Appropriate Ages

There are n persons on a social media website. You are given an integer array ages where ages[i] is the age of the ith person.

A Person x will not send a friend request to a person y (x != y) if any of the following conditions is true:

age[y] <= 0.5 * age[x] + 7
age[y] > age[x]
age[y] > 100 && age[x] < 100
Otherwise, x will send a friend request to y.

Note that if x sends a request to y, y will not necessarily send a request to x. Also, a person will not send a friend request to themself.

Return the total number of friend requests made.

Example 1:

	Input: ages = [16,16]
	Output: 2
	Explanation: 2 people friend request each other.
	Example 2:

	Input: ages = [16,17,18]
	Output: 2
	Explanation: Friend requests are made 17 -> 16, 18 -> 17.
	Example 3:

	Input: ages = [20,30,100,110,120]
	Output: 3
	Explanation: Friend requests are made 110 -> 100, 120 -> 110, 120 -> 100.
 
Constraints:

	n == ages.length
	1 <= n <= 2 * 104
	1 <= ages[i] <= 120
'''

'''
超时
'''
class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        def issend(x, y):
            a = y <= 0.5 * x + 7
            b = y > x
            c = y > 100 and x < 100
            if a or b or c:
                return 0
            return 1
        ages.sort(reverse=True)
        res = 0
        print(ages)
        for i in range(len(ages)-1):
            for j in range(i+1, len(ages)):
                if i == j:
                    continue
                
                res += issend(ages[i], ages[j])
                #print(i, j, res)
        return res

'''
用map

条件一定就规矩按照原题目写
不能将if里面的 y==x单独拆开
拆开的条件应该是 (y>0.5*x+7 and y<x) 和 (y>0.5*x+7 and y==x) 
之前写的y==x的条件时，忘记了y>0.5*x+7
'''
from collections import Counter
class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        res = 0
        for x, cx in count.items():
            for y, cy in count.items():
                if  y > 0.5 * x + 7 and y <= x :
                    if x == y:
                        res += cx * (cx - 1)
                    else:
                        res += cx * cy       
        return res