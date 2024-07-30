'''
Given a string s, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
'''


'''
 如果非字母，使用s.lower()也会返回原值。 
 .lower()可对长字符串使用
'''
def isPalindrome(s: str) -> bool:
    sample = 'abcdefghijklmnopqrstuvwxyz0123456789'
    i = 0
    j = len(s)-1
    if not s:
        return True
    while i <= j:
        while i <len(s) and not s[i].lower() in sample:
            i = i + 1
        while j >=0 and not s[j].lower() in sample:
            j = j - 1
        if i < len(s) and j >=0 and s[i].lower() != s[j].lower():
            return False
        i = i + 1
        j = j - 1
    return True

'''
坑就是还有数字
'''
def isPalindrome(self, s: str) -> bool:
    mark = 'abcdefghijklmnopqrstuvwxyz0123456789'
    ss =  ''.join([x.lower() for x in s if x.lower() in mark]) # .isalnum()
    # print(ss)
    return ss == ss[::-1]