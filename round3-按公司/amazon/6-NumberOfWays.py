'''
https://gongybable.medium.com/amazon-oa-question-different-types-of-pages-y-tech-442d5ffb9a56

The Amazon Kindle Store is an online e-book store where readers can choose a book from a wide range of categories. It also provides the ability to bookmark pages the user wishes to return to later. A book is represented as a binary string having two types of pages:

‘0’: an ordinary page
‘1’: a bookmarked page

Find the number of ways to select 3 pages in ascending index order such that no two adjacent selected pages are of the same type.

Example 1:

book = '01001' 
The following sequences of pages match the criterion: 
[1, 2 ,3], that is, 01001 → 010. 
[1, 2 ,4], that is, 01001 → 010. 
[2, 3 ,5], that is, 01001 → 101. 
[2, 4 ,5], that is, 01001 → 101. 
The answer is 4.
'''
就是看101和010有几种组合

# try the case 101
starting_ones = 0
ending_ones = ones
for page in book_str:
    if page == '0':
        res += starting_ones * ending_ones
    else:
        ending_ones -= 1
        starting_ones += 1

# try the case 010
starting_zeros = 0
ending_zeros = zeros
for page in book_str:
    if page == '1':
        res += starting_zeros * ending_zeros
    else:
        ending_zeros -= 1
        starting_zeros += 1