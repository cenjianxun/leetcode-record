'''
314🔒. Binary Tree Vertical Order Traversal 二叉树的竖直遍历

Given a binary tree, return the vertical order traversal of its nodes' values. (ie, from top to bottom, column by column).

If two nodes are in the same row and column, the order should be from left to right.

Examples 1:

	Input: 
	[3,9,20,null,null,15,7]

	Output:

	[
	  [9],
	  [3,15],
	  [20],
	  [7]
	]

Examples 2:

	Input: 
	[3,9,8,4,0,1,7]

	Output:

	[
	  [4],
	  [9],
	  [3,0,1],
	  [8],
	  [7]
	]

Examples 3:

	Input: 
	[3,9,8,4,0,1,7,null,null,null,2,5]

	Output:

	[
	  [4],
	  [9,5],
	  [3,0,1],
	  [8,2],
	  [7]
	]
'''