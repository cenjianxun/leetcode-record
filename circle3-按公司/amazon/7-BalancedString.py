'''
Given a String S return the number of ways you could split the string into balanced strings. ? could be replaced with ( or ) or [ or ].

So for example let say S = [(?]]??[ split the string into [(?] and ]??[ .

1st way
so for the first string [(?] --> ? could be replaced with ) and it would make it [()]
so for the first string ]??[ --> First ? could be replaced with ] and it would make it ]]?[. Then replace the second ? with ] and it would make it []][ and then interchange ] and [ and would make it [][].
2nd way
so for the first string [(?] --> ? could be replaced with ) and it would make it [()]
so for the first string ]??** --> First ? could be replaced with ( and replace the second ? with ) and it would make it **[ then interchange ] and [ and would make it [()].
'''

要保证a[] b() 和 其它q 都balance，以及一开始的差值 ta-a, tb-b, ta-q也balance