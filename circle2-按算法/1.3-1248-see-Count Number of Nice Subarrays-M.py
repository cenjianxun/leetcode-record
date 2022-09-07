'''
1248. Count Number of Nice Subarrays
Medium

Given an array of integers nums and an integer k. A continuous subarray is called nice if there are k odd numbers on it.

Return the number of nice sub-arrays.

Example 1:

    Input: nums = [1,1,2,1,1], k = 3
    Output: 2
    Explanation: The only sub-arrays with 3 odd numbers are [1,1,2,1] and [1,2,1,1].

Example 2:

    Input: nums = [2,4,6], k = 1
    Output: 0
    Explanation: There is no odd numbers in the array.

Example 3:

    Input: nums = [2,2,2,1,2,2,1,2,2,2], k = 2
    Output: 16

Constraints:

    1 <= nums.length <= 50000
    1 <= nums[i] <= 10^5
    1 <= k <= nums.length
'''

'''
用这个方法记住最后还要添加一次count
可以不用加'#'
'''
class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        res = 0
        gaps = []
        count = 0
        for n in nums:
            if n%2:
                gaps.append(count)
                gaps.append('#')
                count = 0
            else:
                count += 1
        gaps.append(count)
        lo, hi = 2 * 1 - 1, 2 * k - 1
        #print(gaps, lo, hi)
        while hi < len(gaps):
            res += (gaps[lo - 1] + 1) * (gaps[hi + 1] + 1)
            lo, hi = lo + 2, hi + 2
        return res

'''
统计的是前i的奇数的个数。所以当有奇数时，当前就是1，然后累加个数
是 前j位的奇数的个数 - 前i位的奇数的个数 = i-j 位的奇数的个数 = k
所以key是前i位奇数的个数，value是有这个个数的有几个

'''
class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        res = 0
        preOdd = 0
        preOddCount = {0:1}
        for n in nums:
            preOdd += n % 2
            preOddCount[preOdd] = preOddCount.get(preOdd, 0) + 1
            if preOdd - k in preOddCount:
                res += preOddCount[preOdd - k]
            
        print(preOddCount)
        
        return res