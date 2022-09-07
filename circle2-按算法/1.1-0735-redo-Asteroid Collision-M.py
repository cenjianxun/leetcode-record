'''
735. Asteroid Collision
Medium

We are given an array asteroids of integers representing asteroids in a row.

For each asteroid, the absolute value represents its size, and the sign represents its direction (positive meaning right, negative meaning left). Each asteroid moves at the same speed.

Find out the state of the asteroids after all collisions. If two asteroids meet, the smaller one will explode. If both are the same size, both will explode. Two asteroids moving in the same direction will never meet.

Example 1:

	Input: asteroids = [5,10,-5]
	Output: [5,10]
	Explanation: The 10 and -5 collide resulting in 10. The 5 and 10 never collide.

Example 2:

	Input: asteroids = [8,-8]
	Output: []
	Explanation: The 8 and -8 collide exploding each other.

Example 3:

	Input: asteroids = [10,2,-5]
	Output: [10]
	Explanation: The 2 and -5 collide resulting in -5. The 10 and -5 collide resulting in 10.

Constraints:

	2 <= asteroids.length <= 104
	-1000 <= asteroids[i] <= 1000
	asteroids[i] != 0
'''

'''
这道题条件设定的很有意思。所以很多分支。主要是star会消失。所以可以直接设star会消失=0
[10,2,-5]
【-2，-2，1，-2]
'''
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        res = []
        for star in asteroids:
            if not res or res[-1] < 0 or star > 0:
                res.append(star)
            else:
                while res and star and res[-1] > 0:
                    if res[-1] < abs(star):
                        res.pop()
                    elif res[-1] == abs(star):
                        res.pop()
                        star = 0
                    else:
                        star = 0
                if star:
                    res.append(star)
        return res