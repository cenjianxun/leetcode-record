'''
Amazon Prime Video is a subscription video-on-demand over-the-top streaming and rental service. The team at Prime Video is developing a method to divide movies into groups based on the number of awards they have won. A group can consist of any number of movies, but the difference in the number of awards won by any two movies in the group must not exceed k.

The movies can be grouped together irrespective of their initial order. Determin the minimum number of groups that can be formed such that each movie is in exactly only group.

Input:
int awards[n]: the number of awards each movie has earned
int k: the maximum difference in awards counts

Example:
The numbers of awards per movie are awards = [1,5,4,6,8,9,2], and the maximum allowed difference is k=3.

One way to divide the movies into the minimum number of groups is:
The first group can contain [2,1], the max diff between awards of any two movies is 1 which does not exceed k.
The second group can contain [5,4,6], the max diff between awards of any two movies is 2 which does not exceed k.
The third group can contain [8,9], the max diff between awards of any two movies is 1 which does not exceed k.
So the movies can be divided into a minimum of 3 groups.
'''

def groupMoviesWithAwards(awards, k):
	awards.sort()
	res = 0
	start = 0
	for i in range(len(awards)):
		if awards[i] - awards[start] > 3:
			res += 1
			start = i
	return res