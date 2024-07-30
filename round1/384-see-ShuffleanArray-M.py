'''
Given an integer array nums, design an algorithm to randomly shuffle the array. All permutations of the array should be equally likely as a result of the shuffling.

Implement the Solution class:

Solution(int[] nums) Initializes the object with the integer array nums.
int[] reset() Resets the array to its original configuration and returns it.
int[] shuffle() Returns a random shuffling of the array.
'''

# 洗牌算法：https://yjk94.wordpress.com/2017/03/17/%E6%B4%97%E7%89%8C%E7%9A%84%E6%AD%A3%E7%A1%AE%E5%A7%BF%E5%8A%BF-knuth-shuffle%E7%AE%97%E6%B3%95/

# faster than 90.81% of Python3
import random
class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums

    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        return self.nums

    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        nums = self.nums[:]
        random.shuffle(nums)
        return nums

'''
需要替换，而且要除掉的是本身，比如第i个确定了，下个就从i+1个开始随机
'''
# faster than 30.69% of Python3
class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums

    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        return self.nums

    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        nums = self.nums[:]
        # print(self.nums)
        for i in range(0, len(self.nums)):
            j = random.randint(i, len(self.nums)-1)
            nums[i], nums[j] = nums[j], nums[i]
        return nums