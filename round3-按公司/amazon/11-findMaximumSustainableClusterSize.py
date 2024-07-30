'''
Give you a list servers. Their processing power is given as a array of integer, and boot power as a array of integer.
Write a function to return the max length of sub array which's power consumption is less than or equal to max power limit.
Formula to calculate the power consumption for a subArray is:
Max(bootPower[i...j]) + Sum(processPower[i....j]) * length of subArray.

Note: Single server is also a subArray, return 0 if no such subArray can be found.

Example:
bootPower = [2,3,4,6,1,2];
processPower = [1,3,5,6,4,2];
powerMax = 25
'''

maxl = 0

res = getMax(bootPPower[i:j+1]) + getSum(processPower[i:j+1])
if res <= pwerMax and j - i + 1 > maxl:
	maxl = j - i + 1
return maxl