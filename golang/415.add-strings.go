/*
 * @lc app=leetcode id=415 lang=golang
 *
 * [415] Add Strings
 *
 * https://leetcode.com/problems/add-strings/description/
 *
 * algorithms
 * Easy (51.83%)
 * Likes:    4926
 * Dislikes: 730
 * Total Accepted:    645.7K
 * Total Submissions: 1.2M
 * Testcase Example:  '"11"\n"123"'
 *
 * Given two non-negative integers, num1 and num2 represented as string, return
 * the sum of num1 and num2 as a string.
 *
 * You must solve the problem without using any built-in library for handling
 * large integers (such as BigInteger). You must also not convert the inputs to
 * integers directly.
 *
 *
 * Example 1:
 *
 *
 * Input: num1 = "11", num2 = "123"
 * Output: "134"
 *
 *
 * Example 2:
 *
 *
 * Input: num1 = "456", num2 = "77"
 * Output: "533"
 *
 *
 * Example 3:
 *
 *
 * Input: num1 = "0", num2 = "0"
 * Output: "0"
 *
 *
 *
 * Constraints:
 *
 *
 * 1 <= num1.length, num2.length <= 10^4
 * num1 and num2 consist of only digits.
 * num1 and num2 don't have any leading zeros except for the zero itself.
 *
 *
 */

// @lc code=start
import "fmt"

func addStrings(num1 string, num2 string) string {
	res, carry := "", 0

	for i1, i2 := len(num1)-1, len(num2)-1; i1 >= 0 || i2 >= 0; i1, i2 = i1-1, i2-1 {
		x, y := 0, 0
		if i1 >= 0 {
			x = int(num1[i1] - '0')
		}
		if i2 >= 0 {
			y = int(num2[i2] - '0')
		}
		sum := x + y + carry
		// fmt.Println(x, y, sum)
		res = fmt.Sprintf("%d%s", sum%10, res)
		carry = sum / 10
	}

	if carry > 0 {
		res = fmt.Sprintf("%d%s", carry%10, res)
	}
	return res
}

// @lc code=end

// 此题我的牛角尖：不能直接转成int，但是单个字符可以转成int
// 单个字符转成int的方法：char - '0'
// 进位的英文：carry
// * 要考虑所有的加完之后，进位的情况。

