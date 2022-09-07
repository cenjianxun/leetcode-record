# https://www.youtube.com/playlist?list=PLNmW52ef0uwsjnM06LweaYEZr-wjPKBnj

'''
1. find the number of 1s in the binary representation of a number
eg. 
ones(2) = 1
ones(5) = 2
2 = 0b10
3 = 0b11
=========
how am I gonna extract the individual bits from our number

look at the lowest order bit in the number on each iteration

shift this to the right by 1 and now the lowest order bit is the next value

go through all of the bits in the number

do a while loop, calculate the sum

we're gonna be shifting X each time by one so eventually it's gonna get to zero and then we know that they're no more ones in the binary representation so let's go ahead

mod the number by two
'''

'''
6 = 110
6//2 = 3, 6%2 = 0
3//2 = 1, 3%2 = 1
1//2 = 0, 1%2 = 1
'''
 
def ones(x):
	binx = 0

	while x:
		x, rest = divmod(x, 2)
		binx = binx * 10 + rest
	return binx
x = 3
binx = ones(x)
print(binx)


'''
2. whether a linked list is a palindrome.

push items on to the stack
increment by one
in this state 情况下
'''
class Linklist:
	def __init__(self, val=0):
		self.val = val
		self.next = None

def isPalindrome(head):
	if not head:
		return False
	alist = []
	node = head
	while node:
		alist.append(node.val)
		node = node.next
 
'''
3. if it is a binary search tree

！！！树的值的类型
！！！二叉树重复值怎么处理

in order， right side

if all of the nodes to the right of a given parent node are greater than that node 
and all the nodes to the left of a given parent are less than or equal to that parent node 

how are we going to treat duplicate values

minimum  maximum

our value has to be between 5 and infinity

we're going to call is binary search tree on the left and on the right and so if all of the children are valid and then the parent is going to be valid

we want to make sure we have a base case

went too far to the right

we need to call this method on the two children

sketch out
'''

def isBST(root):
	def helper(node, minimun, maximum):
		if not node:
			return True
		if node.val >= maximum or node.val < minimun:
			return False
		return helper(node.left, minimun, node.val) and helper(node.right, node.val, maximum)	
	return helper(root, float('-inf'), float('int'))



'''
4. whether two string are anagrams

initialize
convert them both to lowercase

we're going to increment a by 1 and B by 3 and then our second one we're going to decrement a by 2 and B by 2 right so now a is negative 1 and B is +1
'''

from collections import Counter
def isAnagrams(s1, s2):
	if not s1.isalpha() or not s2.isalpha():
		return False
	s1, s2 = s1.lower(), s2.lower()
	countS1 = Counter(s1)
	countS2 = Counter(s2)
	return countS1 == countS2

'''
5. longest common substring

eg. substring('ABAB', 'BABA')

1. 考虑字符类型
2. 字符串长度（需要优化）
3. 如果有多个都满足条件怎么办 if we have multiple max length substrings 

brute force
go through all possible substrings
possible approach

we know that since this previous one was a substring so here was a substring then since this is also a substring it's going to be a one longer substring so we're actually going to get this value and we're going to just add one to it
2d array

we're not going to do anything unless the two characters are equal right unless the character at I in string a and the character at J and string B are equal

at the first row or the first column and in either of these cases we don't have a previous cell to refer to 

'''

def longestSubstring(s1, s2):
	res = ''
	if not s1 or not s2:
		return res

	dp = [[0] * (len(s2)+1) for _ in range(len(s1)+1)]
	for i in range(1, len(s1) + 1):
		for j in range(1, len(s2) + 1):
			if s1[i-1] == s2[j-1]:
				dp[i][j] = dp[i-1][j-1] + 1
			if dp[i][j] > len(res):
				res = s1[i - dp[i][j]:i]
	return res

'''
6. find valid order of a graph

eg:{0:[], 1:[0], 2:[0], 3:[1,2], 4:[3]}

start by picking an arbitrary/random node
add a temporary mark
go through every node
'''
def validorder(packages):
	res = []
	queue = deque()
	next_point = {}
	degree = {}
	for i in range(5):
		
		if not packages[i]:
			queue.append(i)
		else:
			degree[i] = len(packages[i])
			if v not in next_point:
				next_point[v] = []
			for v in packages[i]:
				next_point[v].append(i)
	while queue:
		num = queue.popleft()
		res.append(num)
		for v in next_point[num]:
			degree[v] -= 1
			if degree[v] == 0:
				queue.append(v)


'''
7. find the median of two sorted arrays

eg. arr1 = [1, 3, 5], arr2 = [2, 4, 6]
	median(arr1, arr2) = 3.5

continually adds the lesser of the two elements to the array

one over 比中间还多一个
'''

'''
8. find duplicates in list

eg: dups([1,2,1,1,2,3]) = [1,2]
'''
