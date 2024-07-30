'''
374. guessNumberHigherOrLower

I pick a number from 1 to n. You have to guess which number I picked.

Every time you guess wrong, I will tell you whether the number I picked is higher or lower than your guess.

You call a pre-defined API int guess(int num), which returns three possible results:

-1: Your guess is higher than the number I picked (i.e. num > pick).
1: Your guess is lower than the number I picked (i.e. num < pick).
0: your guess is equal to the number I picked (i.e. num == pick).
Return the number that I picked.
'''

def guessNumber(int n):
	left, right = 1, n
	while left < right:
		mid = (left + right) // 2
		if guess(mid) == 0:
			left = right = mid
		elif guess(mid) > 0:
			left = mid + 1
		else:
			right = mid
	return left


def guessNumber(int n):
	left, right = 1, n
	while left < right:
		mid = (left + right) // 2
		if guess(mid) > 0:
			left = mid + 1
		else:
			right = mid
	return left

'''
这题无语的是要调用一个内部定义的函数guess()。

边界处理的点：
各种处理差不多都是因为是向下取整

left的取值问题：
left=mid+1，要往上推一下。反例[1,2]取mid为1，left=mid的话就无限循环了。

命中的时候和哪边合并的问题：
比如说target=6时，逼近途径的情况：
① [6, 6] 退出循环
② [5, 6] 此时mid=5，下一轮left=mid+1=6，进入情况①
③ [5, 7] 此时mid=6命中。如果选left=mid+1就不对，应该是right=mid，进入情况①
④ [6, 7] 此时mid=6命中。如果选left=mid+1也不对，应该是right=mid，进入情况①
综上命中的情况应该和right一样，可以合并。
逻辑上思考应该是，都已经命中了，再+1就偏移的太多了，不可能是。

return谁的问题：
由上一个问题可见，所有退出循环的情况都是left=right=target，所以return谁都一样。


'''