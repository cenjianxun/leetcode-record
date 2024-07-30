/*
 * @lc app=leetcode id=482 lang=golang
 *
 * [482] License Key Formatting
 *
 * https://leetcode.com/problems/license-key-formatting/description/
 *
 * algorithms
 * Easy (43.49%)
 * Likes:    1076
 * Dislikes: 1392
 * Total Accepted:    273.8K
 * Total Submissions: 627.4K
 * Testcase Example:  '"5F3Z-2e-9-w"\n4'
 *
 * You are given a license key represented as a string s that consists of only
 * alphanumeric characters and dashes. The string is separated into n + 1
 * groups by n dashes. You are also given an integer k.
 *
 * We want to reformat the string s such that each group contains exactly k
 * characters, except for the first group, which could be shorter than k but
 * still must contain at least one character. Furthermore, there must be a dash
 * inserted between two groups, and you should convert all lowercase letters to
 * uppercase.
 *
 * Return the reformatted license key.
 *
 *
 * Example 1:
 *
 *
 * Input: s = "5F3Z-2e-9-w", k = 4
 * Output: "5F3Z-2E9W"
 * Explanation: The string s has been split into two parts, each part has 4
 * characters.
 * Note that the two extra dashes are not needed and can be removed.
 *
 *
 * Example 2:
 *
 *
 * Input: s = "2-5g-3-J", k = 2
 * Output: "2-5G-3J"
 * Explanation: The string s has been split into three parts, each part has 2
 * characters except the first part as it could be shorter as mentioned
 * above.
 *
 *
 *
 * Constraints:
 *
 *
 * 1 <= s.length <= 10^5
 * s consists of English letters, digits, and dashes '-'.
 * 1 <= k <= 10^4
 *
 *
 */

// @lc code=start
import "unicode"

func licenseKeyFormatting(s string, k int) string {
	res := ""
	count := 0
	for i := len(s) - 1; i >= 0; i-- {
		if s[i] == '-' {
			continue
		}
		if count == k {
			count = 0
			res = "-" + res
		}
		res = string(unicode.ToUpper(rune(s[i]))) + res
		count = count + 1

	}
	return res
}

// @lc code=end

// 必须要把==k放在最前，否则会miss掉"--a-a"这种开头有好几个"-"的情况
// unicode的变大小写只能是rune格式
// 要byte变rune就 rune(aByte)
