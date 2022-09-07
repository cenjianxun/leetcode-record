'''
605. Can Place Flowers
Easy

You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.

Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule.

Example 1:

    Input: flowerbed = [1,0,0,0,1], n = 1
    Output: true
Example 2:

    Input: flowerbed = [1,0,0,0,1], n = 2
    Output: false
 

Constraints:

    1 <= flowerbed.length <= 2 * 104
    flowerbed[i] is 0 or 1.
    There are no two adjacent flowers in flowerbed.
    0 <= n <= flowerbed.length
'''

'''
方法好曲折
'''
class Solution:
    def canPlaceFlowers(self, f: List[int], n: int) -> bool:
        zero = []
        for i in range(len(f)-1):
            if f[i] == 0 and f[i+1] == 1:
                f[i] = -1
            if f[i] == 1 and f[i+1] == 0:
                f[i+1] = -1
        for i in range(len(f)):
            if f[i] == 0:
                zero.append(i)
        
        print(zero)
        while n and zero:
            i = zero.pop()
            n -= 1
            if zero and i-1 == zero[-1]:
                zero.pop()
        return n==0


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count = 0
        for i in range(len(flowerbed)):
            # Check if the current plot is empty.
            if flowerbed[i] == 0:
                # Check if the left and right plots are empty.
                empty_left_plot = (i == 0) or (flowerbed[i - 1] == 0)
                empty_right_lot = (i == len(flowerbed) - 1) or (flowerbed[i + 1] == 0)
                
                # If both plots are empty, we can plant a flower here.
                if empty_left_plot and empty_right_lot:
                    flowerbed[i] = 1
                    count += 1
                    
        return count >= n