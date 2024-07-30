'''
767. Reorganize String

Given a string s, rearrange the characters of s so that any two adjacent characters are not the same.

Return any possible rearrangement of s or return "" if not possible.

Example 1:

	Input: s = "aab"
	Output: "aba"
	Example 2:

	Input: s = "aaab"
	Output: ""

'''

# faster than 67.64% of Python3 online submissions for Reorganize String.
    def reorganizeString(self, s: str) -> str:
        matrix = sorted([[val] * c for val, c in Counter(s).items()], key=len, reverse=True)
        print(matrix)
        if len(matrix[0]) > len(s)//2 + len(s)%2:
            return ''
        diff = len(matrix[0]) - len(matrix[1])
        last = matrix.pop()
        print(diff, last)
        while diff > 1:
            if not last:
                last = matrix.pop()
            matrix[1].append(last.pop())
            diff -= 1
        if last:
            matrix.append(last)
        print(matrix)
        res = ''
        print(len(matrix))
        for i in range(len(matrix[0])):
            for j in range(len(matrix)):
                if len(matrix[j]) <= i or not matrix[j][i]:
                    break
                res = res + matrix[j][i]
        return res


'''
hhhhhhhhhhh 看discussion时先找lee215或者StefanPochmann。。。每次看完都觉得自己好蠢
'''
    def reorganizeString(self, s: str) -> str:
    	# When two characters have the same count, they will remain the relative order since the keys are equal during comparison. (e.g. 'abba' --> ['a', 'b', 'b', 'a'])
        a = sorted(sorted(s), key=s.count)
        h = len(a) // 2
        # 单双插入，要把更frequency的放前面，所以要a[1::2]对应a[h:]
        a[1::2], a[::2] = a[:h], a[h:]
        # When the size of a is just 1, using a[-1] != a[-2] will lead to array index out of range.
        return ''.join(a) * (a[-1:] != a[-2:-1])