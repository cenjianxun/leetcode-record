/*
 * @lc app=leetcode id=1 lang=golang
 *
 * [1] Two Sum
 *
 * https://leetcode.com/problems/two-sum/description/
 *
 * algorithms
 * Easy (51.35%)
 * Likes:    53979
 * Dislikes: 1797
 * Total Accepted:    11.7M
 * Total Submissions: 22.9M
 * Testcase Example:  '[2,7,11,15]\n9'
 *
 * Given an array of integers nums and an integer target, return indices of the
 * two numbers such that they add up to target.
 *
 * You may assume that each input would have exactly one solution, and you may
 * not use the same element twice.
 *
 * You can return the answer in any order.
 *
 *
 * Example 1:
 *
 *
 * Input: nums = [2,7,11,15], target = 9
 * Output: [0,1]
 * Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
 *
 *
 * Example 2:
 *
 *
 * Input: nums = [3,2,4], target = 6
 * Output: [1,2]
 *
 *
 * Example 3:
 *
 *
 * Input: nums = [3,3], target = 6
 * Output: [0,1]
 *
 *
 *
 * Constraints:
 *
 *
 * 2 <= nums.length <= 10^4
 * -10^9 <= nums[i] <= 10^9
 * -10^9 <= target <= 10^9
 * Only one valid answer exists.
 *
 *
 *
 * Follow-up: Can you come up with an algorithm that is less than O(n^2) time
 * complexity?
 */

// @lc code=start
func twoSum(nums []int, target int) []int {
	marked := map[int]int{}
	for i, v := range nums {
		sub := target - v
		if j, ok := marked[sub]; ok {
			return []int{j, i}
		} else {
			marked[v] = i
		}
	}
	return nil
}

// @lc code=end

//
//
// 暴力解法
//
// func twoSum(nums []int, target int) []int {
// 	n := len(nums)
// 	for i, v := range nums {
// 		for j := i + 1; j < n; j++ {
// 			if v+nums[j] == target {
// 				return []int{i, j}
// 			}
// 		}
// 	}
// 	// dont forget here
// 	return nil
// }

