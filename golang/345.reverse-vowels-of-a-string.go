/*
 * @lc app=leetcode id=345 lang=golang
 *
 * [345] Reverse Vowels of a String
 *
 * https://leetcode.com/problems/reverse-vowels-of-a-string/description/
 *
 * algorithms
 * Easy (52.00%)
 * Likes:    4342
 * Dislikes: 2753
 * Total Accepted:    764.2K
 * Total Submissions: 1.5M
 * Testcase Example:  '"hello"'
 *
 * Given a string s, reverse only all the vowels in the string and return it.
 *
 * The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both
 * lower and upper cases, more than once.
 *
 *
 * Example 1:
 * Input: s = "hello"
 * Output: "holle"
 * Example 2:
 * Input: s = "leetcode"
 * Output: "leotcede"
 *
 *
 * Constraints:
 *
 *
 * 1 <= s.length <= 3 * 10^5
 * s consist of printable ASCII characters.
 *
 *
 */

// @lc code=start
import "strings"

func reverseVowels(s string) string {
	res := ""
	set := map[byte]bool{
		'a': true,
		'e': true,
		'i': true,
		'o': true,
		'u': true,
		'A': true,
		'E': true,
		'I': true,
		'O': true,
		'U': true,
	}
	// vowels := "aeiouAEIOU"
	j := len(s) - 1
	for i := 0; i < len(s); i++ {
		if set[s[i]] {
			for !set[s[j]] && j >= 0 {
				j--
			}
			res = res + string(s[j])
			j--
		} else {
			res = res + string(s[i])
		}
	}
	return res
}

// @lc code=end

// 这个题记一下go版本的笔记。
// 好的方法是将string切片，组装好之后再转换为string
// string内单个字母的类型是byte



