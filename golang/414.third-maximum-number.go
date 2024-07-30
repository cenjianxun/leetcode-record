/*
 * @lc app=leetcode id=414 lang=golang
 *
 * [414] Third Maximum Number
 *
 * https://leetcode.com/problems/third-maximum-number/description/
 *
 * algorithms
 * Easy (34.21%)
 * Likes:    2908
 * Dislikes: 3056
 * Total Accepted:    497.7K
 * Total Submissions: 1.5M
 * Testcase Example:  '[3,2,1]'
 *
 * Given an integer array nums, return the third distinct maximum number in
 * this array. If the third maximum does not exist, return the maximum
 * number.
 *
 *
 * Example 1:
 *
 *
 * Input: nums = [3,2,1]
 * Output: 1
 * Explanation:
 * The first distinct maximum is 3.
 * The second distinct maximum is 2.
 * The third distinct maximum is 1.
 *
 *
 * Example 2:
 *
 *
 * Input: nums = [1,2]
 * Output: 2
 * Explanation:
 * The first distinct maximum is 2.
 * The second distinct maximum is 1.
 * The third distinct maximum does not exist, so the maximum (2) is returned
 * instead.
 *
 *
 * Example 3:
 *
 *
 * Input: nums = [2,2,3,1]
 * Output: 1
 * Explanation:
 * The first distinct maximum is 3.
 * The second distinct maximum is 2 (both 2's are counted together since they
 * have the same value).
 * The third distinct maximum is 1.
 *
 *
 *
 * Constraints:
 *
 *
 * 1 <= nums.length <= 10^4
 * -2^31 <= nums[i] <= 2^31 - 1
 *
 *
 *
 * Follow up: Can you find an O(n) solution?
 */

// @lc code=start
import "math"

func thirdMax(nums []int) int {
	max1, max2, max3 := math.MinInt64, math.MinInt64, math.MinInt64
	for _, n := range nums {
		if n > max1 {
			max1, max2, max3 = n, max1, max2
		} else if n > max2 {
			if n != max1 {
				max1, max2, max3 = max1, n, max2
			}
		} else if n > max3 {
			if n != max2 {
				max1, max2, max3 = max1, max2, n
			}
		}
	}

	if max3 != math.MinInt64 {
		return max3
	} else if max1 != math.MinInt64 {
		return max1
	} else {
		return 0
	}
}

// @lc code=end

