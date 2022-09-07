'''
475. Heaters
Medium

Winter is coming! During the contest, your first job is to design a standard heater with a fixed warm radius to warm all the houses.

Every house can be warmed, as long as the house is within the heater's warm radius range. 

Given the positions of houses and heaters on a horizontal line, return the minimum radius standard of heaters so that those heaters could cover all houses.

Notice that all the heaters follow your radius standard, and the warm radius will the same.

Example 1:

    Input: houses = [1,2,3], heaters = [2]
    Output: 1
    Explanation: The only heater was placed in the position 2, and if we use the radius 1 standard, then all the houses can be warmed.

Example 2:

    Input: houses = [1,2,3,4], heaters = [1,4]
    Output: 1
    Explanation: The two heater was placed in the position 1 and 4. We need to use radius 1 standard, then all the houses can be warmed.

Example 3:

    Input: houses = [1,5], heaters = [2]
    Output: 3
 
Constraints:

    1 <= houses.length, heaters.length <= 3 * 104
    1 <= houses[i], heaters[i] <= 109
'''

'''
超时
'''
class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses = set(houses)
        warmed = set()
        radius = 0
        heater_warm = {}
        for heater in heaters:
            heater_warm[heater] = [heater, heater]
            if heater in houses:
                warmed.add(heater)
        while houses - warmed:
            radius += 1
            for heater in heater_warm:
                left = heater_warm[heater][0] - 1
                right = heater_warm[heater][1] + 1
                if left > 0 and left in houses:
                    warmed.add(left)
                if right in houses:
                    warmed.add(right)
                heater_warm[heater] = [left, right]
            #print(radius, heater_warm)
            
        return radius


'''
为什么做这么久
：对于每个房屋，要么用前面的暖气，要么用后面的，二者取近的，得到距离
'''
class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()
        i = j = 0
        radius = [float('inf')] * len(houses)
 
        while i < len(houses):
            #print(i,houses[i],j,heaters[j])
            while j < len(heaters) and heaters[j] < houses[i]:
                j = j + 1
            if j < len(heaters):
                radius[i] = min(radius[i], heaters[j]-houses[i])
            if j > 0:
                radius[i] = min(radius[i], houses[i]-heaters[j-1])
            i = i + 1

        print(radius)
        return max(radius)

'''
+ 二分
'''
class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        ans = 0
        heaters.sort()
        for house in houses:
            j = bisect_right(heaters, house)
            i = j - 1
            rightDistance = heaters[j] - house if j < len(heaters) else float('inf')
            leftDistance = house - heaters[i] if i >= 0 else float('inf')
            curDistance = min(leftDistance, rightDistance)
            ans = max(ans, curDistance)
        return ans
