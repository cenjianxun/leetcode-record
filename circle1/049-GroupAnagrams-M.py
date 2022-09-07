'''
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
'''

'''
看看set判断相等的方式
hash
==
is
'''

def groupAnagrams(strs: List[str]) -> List[List[str]]:
    check = []
    result = []
    for s in strs:
        ss = ''.join(sorted(s))
        if ss in check:
            f = check.index(ss) 
        else:
            f = -1
        # print(ss, check, f)
        if f == -1:
            check.append(ss)
            result.append([s])
        else:
            result[f].append(s)
    # print(check)
    return result

def groupAnagrams(strs: List[str]) -> List[List[str]]:
    result = {}
    for s in strs:
        ss = ''.join(sorted(s))
        if not ss in result:
            result[ss] = [s]
        else:
            result[ss].append(s)
    return list(result.values())