'''
https://www.desiqna.in/5059/amazon-oa-coding-questions-and-solutions-set-7-2022

To increase efficiency, the Amazon shipping team will group packages being shipped according to weight. They will merge a lighter package with a heavier package, which eliminates the need for separate shipments.

More formally, consider n packages, where packageWeights[i] represents the weight of the ith package. You can combine the ith and (i+1)th package if packageWeight[i]<packageWeight[i+1], then discard the ith package. After this operation, the number of packages is reduced by 1 and the weight of (i+1)th package increases by packageWeight[i]. You can merge the packages any number of times.

Find the maximum possible weight of a package that can be achieved after any sequence of merge-operations.

For example, packageWeights = [2, 9, 10, 3, 7]
Combine packages at index 1 and index2, and packages at index 3 and index 4: [2, 19, 10]
And then combine packages at index 0 and 1: [21, 10]
The weight of the heaviest package achievable after merging is 21.
'''

def maxPackageWeightMerge(packageWeights):
	maxW = 0
	stack = []
	packageWeights.append(0)
	for w in packageWeights:
		if not stack or w > stack[-1]:
			stack.append(w)
		else:
			maxW = max(maxW, sum(stack))
			stack = []
	print(maxW)
	return maxW

packageWeights = [2, 9, 10, 3, 7]
maxPackageWeightMerge(packageWeights)