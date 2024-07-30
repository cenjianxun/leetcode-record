'''
Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.
'''

'''
insert的插入是插入原list，不会生成新list
insert有两个参数（位置，值），如果遍历的话，是需要（0，len+1）而不是（0，len）
'''
def permute(self, nums: List[int]) -> List[List[int]]:
    def addList(preList, num):
        result = []
        if not preList:
            preList.insert(0, num)
            result.append(preList)
        else:
            print('preList', preList, num)
            for pl in preList:
                # print('pl', pl)
                for i in range(0, len(pl)+1):
                    templ = pl[:]
                    templ.insert(i, num)
                    result.append(templ)    
        return result
    result = []

    for n in nums:
        result = addList(result, n)
    return result 