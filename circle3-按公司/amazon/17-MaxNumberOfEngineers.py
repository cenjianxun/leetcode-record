'''
You are given 3 inputs
int: teamSize:: representing the number of engineers to complete a team, otherwise the team does not count towards total
1 <= teamSize <= 10^4 unsure about constraint
int: maxDiff:: representing the maximum allowed gap in skill between the least skilled engineer on a team and the most skilled on the team

1 <= maxDiff <= 100 unsure about constraint
array[int]: skill:: representing the pool of engineers to build teams from, skill[i] being the skill level an engineer i

1 <= pool of enginers <= 10^4 unsure about constraint
1 <= skill[i] <= 100 unsure about constraint
what is the maximum number of teams that can be constructed from the pool of engineers, respecting the maxDiff rule for each team?
Example1:
input: teamSize: 1, maxDiff: 1, skill: [34, 5, 72, 48, 15, 2]
output: 6 ---> (resulting teams [[2], [5], [15], [34], [48], [72]])

Example2:
input: teamSize: 3, maxDiff: 20, skill: [34, 5, 72, 48, 15, 2]
output: 1 ---> (resulting teams [[2, 5, 15]])

Example3:
input: teamSize: 3, maxDiff: 30, skill: [34, 5, 72, 48, 15, 2]
output: 2 ---> (resulting teams [[2, 5, 15], [34, 48, 72]])

Example4:
input: teamSize: 3, maxDiff: 5, skill: [34, 5, 72, 48, 15, 2]
output: 0 ---> (resulting teams [])

Example5:
input: teamSize: 3, maxDiff: 25, skill: [1, 7, 18, 32, 65, 72, 90, 98, 100, 113, 146]
output: 3 ---> (resulting teams [[7, 18, 32], [65, 72, 90], [98, 100, 113]])
'''

def MaxNumberOfEngineers(size, maxDiff, skill):
	if size == 1:
		return len(skill)
	skill.sort()
	diff = [] 
	for i in range(1, len(skill)):
		diff.append(skill[i] - skill[i-1])
	print(diff)

	preSumOfDiff = [0]
	for num in diff:
		preSumOfDiff.append(preSumOfDiff[-1] + num)
	print(preSumOfDiff)
	r = size - 1
	i = r
	res = 0
	while i < len(preSumOfDiff):
		if preSumOfDiff[i] - preSumOfDiff[i-r] <= maxDiff:
			res += 1
			print(i, preSumOfDiff[i], res)
			i += r
			
		else:
			i += 1
	print(res)
	return res
size = 3
maxDiff = 30
skill = [34, 5, 72, 48, 15, 2]#[1, 7, 18, 32, 65, 72, 90, 98, 100, 113, 146]
MaxNumberOfEngineers(size, maxDiff, skill)