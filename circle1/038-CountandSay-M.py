'''
The count-and-say sequence is a sequence of digit strings defined by the recursive formula:

countAndSay(1) = "1"
countAndSay(n) is the way you would "say" the digit string from countAndSay(n-1), which is then converted into a different digit string.
'''

'''
不是所有的重复 只有连着的重复
'''

def countAndSay(n):
    if n == 1:
        return '1'
    else:
        last_r = list(countAndSay(n-1))
        r = ''
        l = []
        while last_r:
            s = last_r.pop(0)
            if not l or not l[-1][1] == s:
                l.append([1, s])
            elif l[-1][1] == s:
                l[-1][0] = l[-1][0] + 1
        for e in l:
            r = r + str(e[0]) + e[1]
        return r

r = countAndSay(5)
print(r)