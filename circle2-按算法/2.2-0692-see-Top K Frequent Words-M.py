'''
692. Top K Frequent Words
Medium

Given an array of strings words and an integer k, return the k most frequent strings.

Return the answer sorted by the frequency from highest to lowest. Sort the words with the same frequency by their lexicographical order.

Example 1:

	Input: words = ["i","love","leetcode","i","love","coding"], k = 2
	Output: ["i","love"]
	Explanation: "i" and "love" are the two most frequent words.
	Note that "i" comes before "love" due to a lower alphabetical order.

Example 2:

	Input: words = ["the","day","is","sunny","the","the","the","sunny","is","is"], k = 4
	Output: ["the","is","sunny","day"]
	Explanation: "the", "is", "sunny" and "day" are the four most frequent words, with the number of occurrence being 4, 3, 2 and 1 respectively.
 
Constraints:

	1 <= words.length <= 500
	1 <= words[i].length <= 10
	words[i] consists of lowercase English letters.
	k is in the range [1, The number of unique words[i]]
 
Follow-up: Could you solve it in O(n log(k)) time and O(n) extra space?
'''

'''
用堆的话，只能先全部heapify，不能逐个直接heappop list，否则第二个值是未排序的

other: key = lambda x:(条件1，条件2)，只能sorted 不能sort因为是dic
'''
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        counts = collections.Counter(words)
        heap = [(-count, word) for word, count in counts.items()]
        heapq.heapify(heap) #creating heap in place
        return [heapq.heappop(heap)[1] for _ in range(k)]
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        from collections import Counter
        count = Counter(words)
        res = sorted(count, key=lambda x: (-count[x], x))
        return res[:k]